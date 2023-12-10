import os
import subprocess


def get_parent_framework_path():
    current_path = os.getcwd()
    get_parent = os.path.dirname(current_path)
    return get_parent


def get_data_folder_path():
    current_path = os.path.dirname(os.getcwd())
    return os.path.join(current_path, "base_datas")


def create_reports_path():
    framework_path = get_parent_framework_path()
    reports_path = os.path.join(framework_path, "reports")
    if not os.path.exists(reports_path):
        os.makedirs(reports_path)
    return reports_path


def create_recordings_path():
    framework_path = get_parent_framework_path()
    reports_path = os.path.join(framework_path, "reports")
    create_recordings = os.path.join(reports_path, "recordings")
    if not os.path.exists(create_recordings):
        os.makedirs(create_recordings)
    return create_recordings


def create_screenshots_folder():
    framework_path = get_parent_framework_path()
    reports_path = os.path.join(framework_path, "reports")
    screenshot_path = os.path.join(reports_path, "screenshots")
    if not os.path.exists(screenshot_path):
        os.makedirs(screenshot_path)
    return screenshot_path


def generate_encrypted_password(password):
    framework_path = get_parent_framework_path()
    credentials_path = os.path.join(framework_path, "utilities", "credentials_generation.exe")
    execution_command = credentials_path + " encrypt " + password
    output = subprocess.check_output(execution_command, shell=True, stderr=subprocess.STDOUT, text=True)
    output.strip()
    return output


def decrypt_password(password):
    framework_path = get_parent_framework_path()
    credentials_path = os.path.join(framework_path, "utilities", "credentials_generation.exe")
    execution_command = credentials_path + " decrypt " + password
    output = subprocess.check_output(execution_command, shell=True, stderr=subprocess.STDOUT, text=True)
    output.strip()
    return output
