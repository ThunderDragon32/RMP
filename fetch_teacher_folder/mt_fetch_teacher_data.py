# *****************************************************************************
# File: mt_fetch_teacher_data.py
# Author: Robert Boggs II
# Date: October 04, 2023
# Description: This script fetches Teacher Data from RateMyProfessors.
# *****************************************************************************

import threading
from teacher_print_functions import *
from teacher_inital_payload import generate_inital_payload
from teacher_rating_payload import generate_teacher_rating_payload
from teacher_csv_functions import *
import requests
import json
from time import sleep

# Define the GraphQL endpoint URL and headers here
graphql_url = "https://www.ratemyprofessors.com/graphql"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Authorization": "Basic dGVzdDp0ZXN0",
        "Cookie": "_ga=GA1.1.1667084848.1690933012; ...",  
        "Referer": "https://www.ratemyprofessors.com/professor/92"
}

class Color:
    RED = '\033[31m'
    GREEN = '\033[32m'
    RESET = '\033[0m'


# Define a function to fetch teacher data
def fetch_teacher_data(teacher_id, cursor):

  #=========Inital Request (Basic Teacher Data, No Student Ratings)

    inital_payload = generate_inital_payload(teacher_id)

    while True:

        try:
            response = requests.post(graphql_url, json=inital_payload, headers=headers)

            if response.status_code == 200:
                try:
                    data = response.json()
                    teacher_node = data['data']['node']

                    if teacher_node:
                        # Process teacher data
                        teacher_csv_writer("teacher.csv", teacher_node)
                        teacher_course_codes_csv_writer("teacher_course_codes.csv", teacher_node)
                        teacher_rating_tags_csv_writer("teacher_rating_tags.csv", teacher_node)
                        teacher_related_teachers_csv_writer("teacher_related_teachers.csv", teacher_node)
                        break

                    else:
                        print(f"{Color.RED} Received 'Professor not found' message for {teacher_id} skipping inital request...\n{data}{Color.RESET}")
                        break

                except json.decoder.JSONDecodeError:
                    print(f"{Color.RED} Invalid JSON Response for Inital Request..skipping..{Color.RESET}")
                    break

            else:
                print(f"{Color.RED} GraphQL request failed with status code {response.status_code}{Color.RESET}")
                break


        except requests.exceptions.RequestException as e:
            print(f"{Color.RED} An error occurred during the initial request retrying:{Color.RESET}", e)
            sleep(5)
            continue
        except PermissionError as pe:
            print(f"{Color.RED} Did you open the file? Permission Error, retrying:{Color.RESET}", pe)
            sleep(5)
            continue

#=====Second Request (All Teacher's Specific Ratings)
            
    while True: #While there are more ratings available (if has_next_page)
        try:

            rating_payload = generate_teacher_rating_payload(teacher_id, cursor) #get_teacher_rating_payload(teacher_id, cursor): NOTE: cursor = "" is BEGINNING
            # Send the GraphQL request
            response = requests.post(graphql_url, json=rating_payload, headers=headers)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                try:
                    data = response.json()
                    # print(data) #Debug print
                    teacher_node = data['data']['node'] # Grab teacher_node to access data
                    if teacher_node:
                        #print(teacher_node) #Debug print

                        #Print Function, prints to the console
                        #------------------------------------------------------------
                        # print_student_ratings(teacher_node)
                        #------------------------------------------------------------
      
                        # CSV Writer Functions to write data to a CSV file
                        #------------------------------------------------------------
                        student_ratings_csv_writer("teacher_student_ratings.csv", teacher_node)
                        #------------------------------------------------------------

                        # print_teacher_page_info(teacher_node)
                        has_next_page = teacher_node['ratings']['pageInfo']['hasNextPage'] # If next page True otherwise False
              
                        if has_next_page: # If next page get current cursor and update cursor to get next set of ratings
                            # print(teacher_node['ratings']['pageInfo']['endCursor'])
                            cursor = teacher_node['ratings']['pageInfo']['endCursor'] # Get the new cursor postion
      
                        else: # No more ratings BREAK OUT of While Loop
                            break

                    else:
                        print(f"{Color.RED} Received 'Professor not found' message for {teacher_id} skipping 2nd request...\n{data}{Color.RESET}")
                        break

                except json.decoder.JSONDecodeError:
                    print(f"{Color.RED} Invalid JSON data response for second request..skipping{Color.RESET}")
                    break

            else:
                print(f"{Color.RED} GraphQL request failed with status code:{Color.RESET}", response.status_code)
                break

        except requests.exceptions.RequestException as e:
            print(f"{Color.RED} An error occurred during the 2nd request retrying:{Color.RESET}", e)
            sleep(5)
            continue
        except PermissionError as pe:
            print(f"{Color.RED} Did you open the file? Permission Error, retrying:{Color.RESET}", pe)
            sleep(5)
            continue

#----------------------------------------------------------------

if __name__ == "__main__":
    fetch_teacher_data("VGVhY2hlci03NA==", "")
    print(f"{Color.GREEN}Completed{Color.RESET}")
