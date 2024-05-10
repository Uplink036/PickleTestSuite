import os
import pickle
import csv
import pandas as pd
import difflib 
  

ERRORS_FOUND = []

def compare_hash(selected_file = None, protocol=pickle.DEFAULT_PROTOCOL):
    operatingsys_folder = os.listdir("logs")
    operatingsys_folder = ["linux", "macOS"]
    with open(selected_file) as file_1: 
        file_1_text = file_1.readlines() 
    for os_folder in operatingsys_folder:
        for pyversion in os.listdir(f"logs/{os_folder}"):
            current_file = f'logs/{os_folder}/{pyversion}/protocol_{protocol}/data.csv'
            with open(current_file) as file_2: 
                file_2_text = file_2.readlines() 
            for line in difflib.unified_diff( 
                file_1_text, file_2_text, fromfile=selected_file,  
                tofile=current_file, lineterm='\n'): 
                global ERRORS_FOUND
                ERRORS_FOUND.append([selected_file, current_file, line])

def compare_all(protocol=pickle.DEFAULT_PROTOCOL):
    operatingsys_folder = os.listdir("logs")
    operatingsys_folder = ["linux", "macOS"]
    for os_folder in operatingsys_folder:
        for pyversion in os.listdir(f"logs/{os_folder}"):
            compare_hash(f"logs/{os_folder}/{pyversion}/protocol_{protocol}/data.csv", protocol)

    for error in ERRORS_FOUND:
        print(error)

    if ERRORS_FOUND == []:
        print("No errors found")


if __name__ == "__main__":

    compare_all(3)
    