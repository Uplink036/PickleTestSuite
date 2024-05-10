import os
import pickle
import csv
import pandas as pd
import difflib 
  

ERRORS_FOUND = []

def compare_hash_lines(selected_file = None, sel_os = None, sel_py = None, protocol=pickle.DEFAULT_PROTOCOL):
    operatingsys_folder = os.listdir("logs")
    with open(selected_file) as file_1: 
        file_1_text = file_1.readlines() 
    for os_folder in operatingsys_folder:
        for pyversion in os.listdir(f"logs/{os_folder}"):
            current_file = f'logs/{os_folder}/{pyversion}/protocol_{protocol}/data.csv'
            with open(current_file) as file_2: 
                file_2_text = file_2.readlines() 
            for line in file_2_text:
                if line not in file_1_text:
                    global ERRORS_FOUND
                    ERRORS_FOUND.append([sel_os, sel_py, os_folder, pyversion, protocol, line])
                    print(sel_os, sel_py, os_folder, pyversion, protocol, line)

def compare_all(protocol=pickle.DEFAULT_PROTOCOL):
    operatingsys_folder = os.listdir("logs")
    for os_folder in operatingsys_folder:
        for pyversion in os.listdir(f"logs/{os_folder}"):
            compare_hash_lines(f"logs/{os_folder}/{pyversion}/protocol_{protocol}/data.csv", os_folder, pyversion, protocol)
            global ERRORS_FOUND
            if ERRORS_FOUND == []:
                print("No errors found")
            else:
                with open(f'hash_data_protocol_{protocol}.csv', 'w') as f:
                    writer_object = csv.writer(f)
                    headers = ["sel_os", "sel_py", "cur_os", "cur_py", "protocol", "diffhash"]
                    writer_object.writerow(headers)
                    writer_object.writerows(ERRORS_FOUND)
                
                ERRORS_FOUND = []

            print(pyversion)


if __name__ == "__main__":

    for protocol in range(0, pickle.HIGHEST_PROTOCOL + 1):
        try:
            compare_all(protocol)
        except:
            pass