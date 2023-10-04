# *****************************************************************************
# File: fetch_all_school_data.py
# Author: Robert Boggs II 
# Date: August 22, 2023
# Description: This script fetches All School data from RateMyProfessors using the school_id_list to get school IDs.
# *****************************************************************************
import winsound
import os
from fetch_school_data import fetch_school_data # import the fetch_school_data function from fetch_school_data.py

#================================================================
# fetch_school_data can be used to retieve a single school's data at a time. 
# We use it here to loop for the amount of school ids in school_id_list and use the school id listed in the file to get each specific school's data.
# The cursor is used to select the starting positon of the school's ratings when displayed 
#================================================================

class Color:
    RED = '\033[31m'
    GREEN = '\033[32m'
    RESET = '\033[0m'


def fetch_all_school_data():
    
    current_line = 0

    frequency = 800  # Set the frequency (in Hz), used for winsound.beep (makes a simple beep sound)
    duration = 1000  # Set the duration (in milliseconds) used for winsound.beep (makes a simple beep sound)

    file_path = 'fetch_school_folder\\school_id_list.txt'
    try: 
        with open(file_path, 'r') as file:
            lines = file.readlines()
            amount_of_lines_in_file = len(lines)

            for school_id in lines: # For every school_id in school_id_list (generated after you run school_id_setup.py) it will get the school_id of the current line
                current_line += 1
                fetch_school_data(school_id.strip(), "") #Takes school_id, and cursor (position to grab data). 
       

                # #Comment out this loop if you dont want it to ask for continue input
                # #================================================================ 
                # winsound.Beep(frequency, duration)
                # continue_outer = False  # Flag to control the outer loop
                # while True: # The inner loop for input continue
                #     ask_to_continue = input("Continue? (y/n): ")
                #     if ask_to_continue == 'y':
                #         break  # Break out of the inner loop
                #     elif ask_to_continue == 'n':
                #         continue_outer = True  # Set the flag to break the outer loop
                #         break  # Break out of the inner loop
                # if continue_outer:
                #     break  # Break out of the outer loop
                # #================================================================

                print(f"                                                {Color.GREEN} {current_line} / {amount_of_lines_in_file} {Color.RESET}") 

    
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.\n-----\nPlease run fetch_school_folder\\school_id_setup.py\n----")

#----------------------------------------------------------------

# This code will only run when fetch_all_school_data.py is executed directly as a script
if __name__ == "__main__":
    fetch_all_school_data()