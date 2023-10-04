# *****************************************************************************
# File: mt_fetch_all_teacher_data.py
# Author: Robert Boggs II 
# Date: October 04, 2023
# Description: This script fetches All Teacher data from RateMyProfessors using the teacher_id_list to get Teacher IDs.
# *****************************************************************************  
from mt_fetch_teacher_data import fetch_teacher_data_with_threads

class Color:
    RED = '\033[31m'
    GREEN = '\033[32m'
    RESET = '\033[0m'
    YELLOW = "\033[93m"

def fetch_all_teacher_data():
    current_line = 0
    inital = True
    file_path = 'fetch_teacher_folder\\teacher_id_list.txt'
    print(f"{Color.YELLOW}ENSURE YOU HAVE A UPDATED COPY OF TEACHER ID LIST BEFORE RUNNING TO LIMIT 'Professor not found' errors{Color.RESET}")

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            amount_of_lines_in_file = len(lines)

            teacher_ids = []  # Initialize a list to hold teacher IDs

            for teacher_id in lines:
                current_line += 1
                teacher_ids.append(teacher_id.strip())  # Add teacher ID to the list
                if inital:
                    inital = False
                    fetch_teacher_data_with_threads(teacher_ids, "")  # Pass the list to the fetch function
                    teacher_ids = []  # Clear the list for the next batch of teacher IDs
                    
                elif len(teacher_ids) == 400:  # If the list reaches a length of 100
                    fetch_teacher_data_with_threads(teacher_ids, "")  # Pass the list to the fetch function
                    teacher_ids = []  # Clear the list for the next batch of teacher IDs
                    total_width = 120

                    batch_completed_text = "Batch Completed"
                    current_line_text = f"{current_line} / {amount_of_lines_in_file}"

                    print(f"{Color.RESET}{batch_completed_text.center(total_width)}\n{Color.GREEN}{current_line_text.center(total_width)}{Color.RESET}")

            # Handle any remaining teacher IDs in the list
            if teacher_ids:
                fetch_teacher_data_with_threads(teacher_ids, "")
                total_width = 120

                batch_completed_text = "Batch Completed"
                current_line_text = f"{current_line} / {amount_of_lines_in_file}"

                print(f"{Color.RESET}{batch_completed_text.center(total_width)}\n{Color.GREEN}{current_line_text.center(total_width)}{Color.RESET}")


    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.\n-----\nPlease run fetch_teacher_folder\\teacher_id_setup.py\n----")

if __name__ == "__main__":
    fetch_all_teacher_data()
