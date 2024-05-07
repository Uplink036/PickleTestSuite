import pickle
import os
import json

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
        print(f"Error in pickling: {error}")
        return

    with open(f'logs/protocol_{protocol}/{folder}/{name}.pkl', 'wb') as f:
        f.write(pickle_object)

def save_unpickled_test(data,protocol=pickle.DEFAULT_PROTOCOL):
    '''Function used to save the data as a pickle and json file in the unpickled folder. This is to be able to verifiy the pickle
    data over different verisons and be able to compare to the json file.'''

    #Check that folder exist
    if not os.path.exists(f"logs/protocol_{protocol}/unpickled"):
        print("Folder does not exist")
        return

    #Check if what is the next number to name the test
    testnumber = 0
    if os.path.exists(f"logs/protocol_{protocol}/unpickled/test_{testnumber}.pkl"):
        while os.path.exists(f"logs/protocol_{protocol}/unpickled/test_{testnumber}.pkl"):
            testnumber += 1

    #Converts the data to pickle and json
    pickle_data = pickle.dumps(data, protocol=protocol)

    #Writes the data to the files
    with open(f'logs/protocol_{protocol}/unpickled/test_{testnumber}.pkl', 'wb') as f:
        f.write(pickle_data)

    #Writes the data to the json file
    json.dump(data, open(f'logs/protocol_{protocol}/unpickled/test_{testnumber}.json', 'w'))


def create_folder(folder_name):
    '''Function used to creat folders in all protocol folders'''
    for i in range(0,6):
        os.mkdir(f"logs/protocol_{i}/{folder_name}")

def test():
    data = {'a': 1, 'b': 2, 'c': 3}
    pickle_saver(data,"fuzzing","test_pickle")


if __name__ == '__main__':
    #create_folder("unpickled")
    #save_unpickled_test({'a': 1, 'b': 2, 'c': 3})
