# *****************************************************************************
# File: mt_fetch_all_teacher_data.py
# Author: Robert Boggs II 
# Date: October 04, 2023
# Description: This script fetches All Teacher data from RateMyProfessors using the teacher_id_list to get Teacher IDs.
# *****************************************************************************  
from mt_fetch_teacher_data import fetch_teacher_data
import threading

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

def fetch_teacher_data_with_threads(teacher_ids, cursor):
    threads = [] # This initalizes an empty list to store thread objects
    for teacher_id in teacher_ids: # For each teacher_ids in the list
        thread = threading.Thread(target=fetch_teacher_data, args=(teacher_id.strip(), cursor)) # This create a new thread
        threads.append(thread) # Appends to the thread list to keep track
        thread.start() # Starts the thread

    for thread in threads: # This will wait and join back all the threads into the main program
        thread.join() #This line waits for each thread to complete its 
                        #execution before moving on. This ensures that all threads have finished fetching teacher data before the program proceeds.

#Main Function
##================================================================

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
                    
                elif len(teacher_ids) == 100:  # If the list reaches a length of 100
                    fetch_teacher_data_with_threads(teacher_ids, "")  # Pass the list to the fetch function
                    teacher_ids = []  # Clear the list for the next batch of teacher IDs
                    print_batch(current_line, amount_of_lines_in_file)

            # Handle any remaining teacher IDs in the list
            if teacher_ids:
                fetch_teacher_data_with_threads(teacher_ids, "")
                print_batch(current_line, amount_of_lines_in_file)

    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.\n-----\nPlease run fetch_teacher_folder\\teacher_id_setup.py\n----")
#============================================================================

if __name__ == "__main__":
    fetch_all_teacher_data()
