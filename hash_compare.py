import os
import pickle
import csv
import pandas as pd

ERRORS_FOUND = []

def compare_hash(selected_file = None, protocol=pickle.DEFAULT_PROTOCOL):
    operatingsys_folder = os.listdir("logs")
    selected_df = pd.read_csv(selected_file)
    for os_folder in operatingsys_folder:
        for pyversion in os.listdir(f"logs/{os_folder}"):
            current_file = f'logs/{os_folder}/{pyversion}/protocol_{protocol}/data.csv'
            current_df = pd.read_csv(current_file)
            try: 
                pd.testing.assert_frame_equal(selected_df, current_df)
            except Exception as e:
                global ERRORS_FOUND
                ERRORS_FOUND.append((selected_file, current_file, e))


def compare_all(protocol=pickle.DEFAULT_PROTOCOL):
    operatingsys_folder = os.listdir("logs")
    for os_folder in operatingsys_folder:
        for pyversion in os.listdir(f"logs/{os_folder}"):
            compare_hash(f"logs/{os_folder}/{pyversion}/protocol_{protocol}/data.csv", protocol)

    for error in ERRORS_FOUND:
        print(error)


if __name__ == "__main__":

    compare_all(3)
    print("No errors found!")