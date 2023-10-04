# *****************************************************************************
# File: main.py
# Author: Robert Boggs II 
# Date: October 04, 2023
# Description: Provides a menu the user can use to select multiple options
#Options Include:
    #Configure ID List,  //This will setup both ID lists that will be used later to fetch data
    #Retrieve Teacher Data, //This will fetch all the teacher data on RMP using the IDs in the teacher_id_list.txt
    #Retrieve School Data, //This will fetch all the school data on RMP using the IDs in the school_id_list.txt
    #Complete RMP Data (No Setup Required), //This will do Options 1-3
    #Quit //Quits the menu

# *****************************************************************************
import keyboard
import time
import os
import sys

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Inserts fetch_school_folder into the python search path
sys.path.insert(1, f'{current_dir}/fetch_school_folder')
# Inserts fetch_teacher_folder into the python search path
sys.path.insert(2, f'{current_dir}/fetch_teacher_folder')

#----School Imports from /fetch_school_folder
import school_id_setup 
import mt_fetch_all_school_data
#-----

#-----Teacher Imports from /fetch_teacher_folder
import teacher_id_setup
import mt_fetch_all_teacher_data
#-----

class Color:
    RED = '\033[31m'
    GREEN = '\033[32m'
    RESET = '\033[0m'
    YELLOW = "\033[93m"

# Function to clear the console screen
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Function to display the menu with a highlighted selection
def display_menu(options, selected_option):
    clear_console()
    print("RMP Scraping Selection Menu:")
    
    for i, option in enumerate(options):
        if i == selected_option:
            print(f"> {option}")  # Highlight the selected option
        else:
            print(f"  {option}")


def option_1():
    print(f"{Color.GREEN}Teacher ID Setup Started{Color.RESET}")
    teacher_id_setup.fetch_teacher_id_list()
    print(f"{Color.GREEN}School ID Setup Started{Color.RESET}")
    school_id_setup.fetch_school_id_list()

def option_2():
    print(f"{Color.GREEN}Fetch All Teacher Data Started{Color.RESET}")
    mt_fetch_all_teacher_data.fetch_all_teacher_data()

def option_3():
    print(f"{Color.GREEN}Fetch All School Data Started{Color.RESET}")
    mt_fetch_all_school_data.fetch_all_school_data()

def option_4():
    option_1()
    option_2()
    option_3()

# Main program loop
options = ["Configure ID List", "Retrieve Teacher Data", "Retrieve School Data", "Complete RMP Data (No Setup Required)", "Quit"]
selected_option = 0

while True:
    display_menu(options, selected_option)

    # Check for arrow key presses
    key_event = keyboard.read_event(suppress=True)
    if key_event.event_type == keyboard.KEY_DOWN and key_event.name == 'down':
        new_option = (selected_option + 1) % len(options)
    elif key_event.event_type == keyboard.KEY_DOWN and key_event.name == 'up':
        new_option = (selected_option - 1) % len(options)
    else:
        new_option = selected_option

    # Check for Enter key press
    if key_event.event_type == keyboard.KEY_DOWN and key_event.name == 'enter':
        if selected_option == 0:
            print(f"You selected {options[selected_option]}.")
            option_1()
            break
        elif selected_option == 1:
            print(f"You selected {options[selected_option]}.")
            option_2()
            break
        elif selected_option == 2:
            print(f"You selected {options[selected_option]}.")
            option_3()
            break
        elif selected_option == 3:
            print(f"You selected {options[selected_option]}.")
            option_4()
            break
        elif selected_option == 4:
            print("The menu was exited.")
            break

    selected_option = new_option
