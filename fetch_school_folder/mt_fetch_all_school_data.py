# *****************************************************************************
# File: mt_fetch_all_school_data.py
# Author: Robert Boggs II 
# Date: October 04, 2023
# Description: This script fetches All School data from RateMyProfessors using the school_id_list to get school IDs.
# *****************************************************************************
from mt__fetch_school_data import fetch_school_data_with_threads # import the fetch_school_data_with_threads function from mt_fetch_school_data.py

#================================================================
# fetch_school_data can be used to retieve a single school's data at a time. 
# We use it here to loop for the amount of school ids in school_id_list and use the school id listed in the file to get each specific school's data.
# The cursor is used to select the starting positon of the school's ratings when displayed 
#================================================================

class Color:
    RED = '\033[31m'
    GREEN = '\033[32m'
    RESET = '\033[0m'
    YELLOW = "\033[93m"

def print_batch(current_line, amount_of_lines_in_file):
    total_width = 120
    batch_completed_text = "Batch Completed"
    current_line_text = f"{current_line} / {amount_of_lines_in_file}"
    print(f"{Color.RESET}{batch_completed_text.center(total_width)}\n{Color.GREEN}{current_line_text.center(total_width)}{Color.RESET}")


def fetch_all_school_data():
    
    current_line = 0
    file_path = 'fetch_school_folder\\school_id_list.txt'
    print(f"{Color.YELLOW}ENSURE YOU HAVE A UPDATED COPY OF SCHOOL ID LIST BEFORE RUNNING TO LIMIT 'School not found' errors{Color.RESET}")

    try: 
        with open(file_path, 'r') as file:
            lines = file.readlines()
            amount_of_lines_in_file = len(lines)
            school_ids = [] # Hold the school IDs for the current batch

            for school_id in lines: # For every school_id in school_id_list (generated after you run school_id_setup.py) it will get the school_id of the current line
                current_line += 1
                school_ids.append(school_id.strip())  # Add school ID to the list
                    
                if len(school_ids) == 400:  # If the list reaches a length of 100
                    fetch_school_data_with_threads(school_ids, "")  # Pass the list to the fetch function
                    school_ids = []  # Clear the list for the next batch of school IDs
                    print_batch(current_line, amount_of_lines_in_file)

            # Handle any remaining school IDs in the list
            if school_ids:
                fetch_school_data_with_threads(school_ids, "")
                print_batch(current_line, amount_of_lines_in_file)


    
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.\n-----\nPlease run fetch_school_folder\\school_id_setup.py\n----")

#----------------------------------------------------------------

# This code will only run when mt_fetch_all_school_data.py is executed directly as a script
if __name__ == "__main__":
    fetch_all_school_data()