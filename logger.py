import pickle
import os
import json
from hashlib import sha256
import sys
import re

def pickle_saver(data,folder,name,protocol=pickle.DEFAULT_PROTOCOL):
    '''Function used to save the data as a pickle file in the specified folder. The data is pickled with the specified protocol.
    If no protocol is specified, the default protocol 4 is used.'''

    if not os.path.exists(f"logs/protocol_{protocol}/{folder}"):
        print("Folder does not exist")
        return

    #Check if the pickle worked, else reporting error
    try:
        pickle_object = pickle.dumps(data, protocol=protocol)
    except Exception as error:
        print(f"Error in pickling/Hasing: {error}")
        return

    with open(f'logs/protocol_{protocol}/{folder}/{name}.pkl', 'wb') as f:
        f.write(pickle_object)

def save_unpickled_test(data,protocol=pickle.DEFAULT_PROTOCOL):
    '''Function used to save the data as a pickle and json file in the unpickled folder. This is to be able to verifiy the pickle
    data over different verisons and be able to compare to the json file.'''
    os_type,version_number = get_os_and_version()

    #Check that folder exist
    if not os.path.exists(f"logs/{os_type}/{version_number}/protocol_{protocol}"):
        print("Folder does not exist")
        return

    #Check if what is the next number to name the test
    testnumber = 0
    if os.path.exists(f"logs/{os_type}/{version_number}/protocol_{protocol}/test_{testnumber}.txt"):
        while os.path.exists(f"logs/{os_type}/{version_number}/protocol_{protocol}/test_{testnumber}.txt"):
            testnumber += 1

    #Check if the pickle worked, else reporting error
    try:
        pickle_object = pickle.dumps(data, protocol=protocol)
        hash_object = sha256(pickle_object).hexdigest()
    except Exception as error:
        print(f"Error in pickling/Hasing: {error}")
        return

    #Writes the data to the files
    with open(f'logs/{os_type}/{version_number}/protocol_{protocol}/test_{testnumber}.txt', 'wb') as f:
        f.write(hash_object.encode("utf-8"))

    #Writes the data to the json file
    json.dump(data, open(f'logs/{os_type}/{version_number}/protocol_{protocol}/test_{testnumber}.json', 'w'))

def unpack_and_commpare_pickle(testnumber=0,protocol=pickle.DEFAULT_PROTOCOL):
    '''Function used to unpack the pickle file and compare it to the json file. The function returns True if the files are the same'''
    os_type,version_number = get_os_and_version()

    with open(f'logs/{os_type}/{version_number}/protocol_{protocol}/test_{testnumber}.txt', 'rb') as f:
        hash_data_prev_py_version = f.read().decode("utf8")

    #Taking the data from the jason and transforming it to a new hash
    json_data = json.load(open(f'logs/{os_type}/{version_number}/protocol_{protocol}/test_{testnumber}.json', 'r'))
    pickle_object = pickle.dumps(json_data, protocol=protocol)
    hash_data_new_py_version = sha256(pickle_object).hexdigest()

    #Checking if the hashes are the same
    assert hash_data_prev_py_version == hash_data_new_py_version

def get_os_and_version():
    os_type = os.name
    if os_type == "posix":
        os_type = "linux"
    elif os_type == "nt":
        os_type = "windows"
    else:
        os_type = "macOS"

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

    for file in os.listdir(f"logs/{os_type}/{version_number}/protocol_{protocol}"):
        os.remove(f"logs/{os_type}/{version_number}/protocol_{protocol}/{file}")


def create_folder(folder_name):
    '''Function used to creat folders in all protocol folders'''
    for i in range(0,6):
        os.mkdir(f"logs/protocol_{i}/{folder_name}")

def test_object():
    data = {'a': 1, 'b': 5, 'c': 3}
    return data


if __name__ == '__main__':
    clean_folder()
    save_unpickled_test(test_object())
    unpack_and_commpare_pickle(0)
    #setup_folders()
