import pytest
import pytest_html
import threading
from utilities.read_input import *
from datetime import datetime
from pages.basic_browser_actions import BasicActions
from utilities.screen_recorder import ScreenRecorder


global driver
driver = None


def pytest_configure(config):
    get_parent = get_parent_framework_path()
    reports_path = os.path.join(get_parent, "reports")
    if not os.path.exists(reports_path):
        os.makedirs(reports_path)
    screen_shot_path = os.path.join(reports_path, "screenshots")
    if not os.path.exists(screen_shot_path):
        os.makedirs(screen_shot_path)
    config.option.htmlpath = reports_path + "/" + "automation_reports.html"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extras", [])
    if report.when == "call":
        extra.append(pytest_html.extras.url("https://stage.myaccount.hp.com"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            report_directory = os.path.join(os.path.dirname(item.config.option.htmlpath), "screenshots")
            try:
                os.mkdir(report_directory)
            except:
                print("directory already presents may be.")
            current_datetime = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            filename = report.nodeid.replace("::", "_")
            if "[" in filename:
                filename = filename[0:filename.index("[")]
            filename = filename[(filename.index(".py") + 4)::] + current_datetime + ".png"
            destination_file = os.path.join(report_directory, filename)
            basic_actions = BasicActions(driver)
            if driver is not None:
                basic_actions.capture_screenshot(destination_file)
            if filename:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height:200px;" onclick="window.open(this.src)" align="right"></div>' % destination_file
            extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_addoption(parser):
    parser.addoption("--environment", action="store", help="environment to execute")
    parser.addoption("--password", action="store", help="Password for tests")


@pytest.fixture(scope="function")
def screen_recorder_config(record_testsuite_property):
    record_testsuite_property("screen_recorder", True)


@pytest.fixture(scope="function")
def open_browser_test_startup(request):
    web_url = get_environment_url()
    global driver
    basic_actions = BasicActions(driver=None)
    driver = basic_actions.open_my_browser()
    basic_actions.go_to_url(web_url)
    basic_actions.maximize_browser_window()
    request.cls.driver = driver
    create_screenshots_folder()
    if fetch_data_from_input_data("video record"):
        recording_path = create_recordings_path()
        environment = fetch_data_from_input_data("environment")
        recording_file = recording_path + "/" + f"{request.node.name}_{environment}.mp4"
        screen_record = ScreenRecorder(recording_file)
        record_thread = threading.Thread(target=screen_record.start_record)
        record_thread.start()
    yield
    if fetch_data_from_input_data("video record"):
        screen_record.stop_record_loop()
    basic_actions.close_browser()

