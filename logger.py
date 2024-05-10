import pickle
import os
import json
import sys
import re
import csv

def save_unpickled_test(data, comment = "",json_data = "", protocol=pickle.DEFAULT_PROTOCOL,):
    '''Function used to save the data as a pickle and json file in the unpickled folder. This is to be able to verifiy the pickle
    data over different verisons and be able to compare to the json file.'''
    os_type,version_number = get_os_and_version()

    #Check that folder exist
    if not os.path.exists(f"logs/{os_type}/{version_number}/protocol_{protocol}"):
        print("Folder does not exist")
        os.makedirs(f"logs/{os_type}/{version_number}/protocol_{protocol}")

    if os.path.exists(f"logs/{os_type}/{version_number}/protocol_{protocol}/data.csv"):
        with open(f'logs/{os_type}/{version_number}/protocol_{protocol}/data.csv', 'a',newline='') as f:
            writer_object = csv.writer(f)
            writer_object.writerow([data, comment,json_data])
    else:
        with open(f'logs/{os_type}/{version_number}/protocol_{protocol}/data.csv', 'w') as f:
            writer_object = csv.writer(f)
            writer_object.writerow([data, comment,json_data])


def get_os_and_version():
    os_type = os.name
    if os_type == "posix":
        os_platform = sys.platform
        if os_platform == "darwin":
            os_type = "macOS"
        else:
            os_type = "linux"
    elif os_type == "nt":
        os_type = "windows"


    version_number = re.search(r'(\d+\.\d+\.\d+)', sys.version).group(0)
    return os_type,version_number

def setup_folders():
    '''Function used to setup the folders for the different protocols'''
    os_type,version_number = get_os_and_version()

    if not os.path.exists(f"logs/{os_type}/{version_number}"):
        for i in range(0,6):
            os.makedirs(f"logs/{os_type}/{version_number}/protocol_{i}")


def clean_folder(protocol=pickle.DEFAULT_PROTOCOL):
    '''Function used to clean the folder of all files'''
    os_type,version_number = get_os_and_version()

    try:
        for file in os.listdir(f"logs/{os_type}/{version_number}/protocol_{protocol}"):
            os.remove(f"logs/{os_type}/{version_number}/protocol_{protocol}/{file}")
        with open(f"logs/{os_type}/{version_number}/protocol_{protocol}/data.csv", 'w') as fp:
            pass
    except FileNotFoundError:
        return


def create_folder(folder_name):
    '''Function used to creat folders in all protocol folders'''
    for i in range(0,6):
        os.mkdir(f"logs/protocol_{i}/{folder_name}")

def test_object():
    data = {'a': 1, 'b': 5, 'c': 3}
    return data


if __name__ == '__main__':
    pass
    #setup_folders()
    #clean_folder()
    #save_unpickled_test(test_object())
    #unpack_and_compare_single_test(0)
    #setup_folders()