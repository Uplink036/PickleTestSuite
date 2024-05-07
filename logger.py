import pickle
import os

def pickle_saver(data,folder,name,protocol=pickle.DEFAULT_PROTOCOL):
    if not os.path.exists(f"logs/protocol_{protocol}/{folder}"):
        print("Folder does not exist")
        return

    try:
        pickle_object = pickle.dumps(data, protocol=protocol)
    except Exception as error:
        print(f"Error in pickling: {error}")
        return

    with open(f'logs/protocol_{protocol}/{folder}/{name}.pkl', 'wb') as f:
        f.write(pickle_object)

def create_folder(folder_name):
    for i in range(0,6):
        os.mkdir(f"logs/protocol_{i}/{folder_name}")

def test():
    data = {'a': 1, 'b': 2, 'c': 3}
    pickle_saver(data,"fuzzing","test_pickle")


# if __name__ == '__main__':
    #create_folder("fuzzing")
