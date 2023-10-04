# *****************************************************************************
# File: fetch_all_teacher_data.py
# Author: Robert Boggs II 
# Date: August 22, 2023
# Description: This script fetches All Teacher data from RateMyProfessors using the teacher_id_list to get Teacher IDs.
# *****************************************************************************  
import winsound
from fetch_teacher_data import fetch_teacher_data

#================================================================
# fetch_teacher_data can be used to retieve a single teacher's data at a time. 
# We use it here to loop for the amount of teacher ids in teacher_id_list and use the teacher id listed in the file to get each specific teacher's data.
# The cursor is used to select the starting positon of the teacher's ratings when displayed 
#================================================================

class Color:
    RED = '\033[31m'
    GREEN = '\033[32m'
    RESET = '\033[0m'



def fetch_all_teacher_data():

    current_line = 0

    frequency = 800  # Set the frequency (in Hz), used for winsound.beep (makes a simple beep sound)
    duration = 1000  # Set the duration (in milliseconds) used for winsound.beep (makes a simple beep sound)

    file_path = 'fetch_teacher_folder\\teacher_id_list.txt'   

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            amount_of_lines_in_file = len(lines)

            for teacher_id in lines: # For every teacher_id in teacher_id_list (generated after you run teacher_id_setup.py) it will get the teacher_id of the current line
                current_line += 1
                fetch_teacher_data(teacher_id.strip(), "") #Takes teacher_id, rating_amount_per_request (amount of ratings to get per request), and cursor (position to grab data). 
        
                # #Comment out this loop if you dont want it to ask for continue input
                # #================================================================ 
                # winsound.Beep(frequency, duration)
                # continue_outer = False  # Flag to control the outer loop
                # while True:
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
        print(f"The file '{file_path}' does not exist.\n-----\nPlease run fetch_teacher_folder\\teacher_id_setup.py\n----")



# This code will only run when fetch_all_teacher_data.py is executed directly as a script
if __name__ == "__main__":
    fetch_all_teacher_data()