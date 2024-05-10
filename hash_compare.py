import os
import pickle
import csv
import pandas as pd

def compare_hash(selected_file = None, protocol=pickle.DEFAULT_PROTOCOL):
    operatingsys_folder = os.listdir("logs")
    selected_df = pd.read_csv(selected_file)
    for os_folder in operatingsys_folder:
        for pyversion in os.listdir(f"logs/{os_folder}"):
            current_df = pd.read_csv(f'logs/{os_folder}/{pyversion}/protocol_{protocol}/data.csv')
            pd.testing.assert_frame_equal(selected_df, current_df, check_exact=True)



def compare_all(protocol=pickle.DEFAULT_PROTOCOL):
    operatingsys_folder = os.listdir("logs")
    for os_folder in operatingsys_folder:
        for pyversion in os.listdir(f"logs/{os_folder}"):
            compare_hash(f"logs/{os_folder}/{pyversion}/protocol_{protocol}/data.csv")


if __name__ == "__main__":
    compare_all()
    print("No errors found!")