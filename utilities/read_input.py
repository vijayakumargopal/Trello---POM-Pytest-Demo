"""
This file contains functions to read input data from input_data.json file.
"""

from utilities.common_functions import *
import json


def get_browser_name():
    file_path = os.path.join(get_data_folder_path(), "input_data.json")
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data["browser"].lower()


def get_environment_url():
    file_path = os.path.join(get_data_folder_path(), "input_data.json")
    with open(file_path, 'r') as file:
        data = json.load(file)
    env = data["environment"].lower()
    return data["environments"][env]


def video_record():
    file_path = os.path.join(get_data_folder_path(), "input_data.json")
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data["video_record"]


def fetch_data_from_input_data(key=None):
    file_path = os.path.join(get_data_folder_path(), "input_data.json")
    with open(file_path, 'r') as file:
        data = json.load(file)
    if key is None:
        return data
    else:
        return data[key]


if __name__=="__main__":
    print(get_browser_name())
