# *****************************************************************************
# File: fetch_teacher_data.py
# Author: Robert Boggs II
# Date: August 22, 2023
# Description: This script fetches Teacher Data from RateMyProfessors.
# *****************************************************************************

import json
from time import sleep  # Import sleep for retry delay
import requests # Used to make HTTP requests
from teacher_print_functions import *  # Simply imports all print functions from teacher_print_functions.py used to display the teacher data
from teacher_inital_payload import generate_inital_payload # import the inital payload function
from teacher_rating_payload import generate_teacher_rating_payload # import the rating payload function
from teacher_csv_functions import * # Simple import all csv functions from teacher_csv_functions

def fetch_teacher_data(teacher_id: str, cursor: str):

    # Define the GraphQL endpoint URL
  graphql_url = "https://www.ratemyprofessors.com/graphql"
    
  # Header set based on given information from requests made on the site for graphql
  headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Authorization": "Basic dGVzdDp0ZXN0",
        "Cookie": "_ga=GA1.1.1667084848.1690933012; ...",  
        "Referer": "https://www.ratemyprofessors.com/professor/92"
    }

  #=========Inital Request (Basic Teacher Data, No Student Ratings)

  inital_payload = generate_inital_payload(teacher_id) ##Give payload the Teacher ID to collect data from the Teacher


  while True:
    try:
      # Send the GraphQL request
      # graph_url is the endpoint url,
      # json=inital_payload is generate_inital_payload(teacher_id)
      # headers is set to header (we defined earlier)
      response = requests.post(graphql_url, json=inital_payload, headers=headers)
      if response.status_code == 200:
        try:
          data = response.json() #Get the data from the response of the request
          # Check if the request was successful (status code 200), this checks to see if we actually got a response back.
          teacher_node = data['data']['node'] # Grab teacher_node to access data
          if teacher_node:
      
            # Print functions to print data to the console
            #--------------------------------------------------------------
            # print_teacher(teacher_node)
            # print_teacher_school(teacher_node)
            # print_teacher_rating_distribution(teacher_node)
            # print_teacher_course_codes(teacher_node)
            # print_teacher_rating_tags(teacher_node)
            # print_related_teachers(teacher_node)
            #----------------------------------------------------------------

            # CSV Writer Functions to write data to a CSV file
            #----------------------------------------------------------------
            teacher_csv_writer("teacher.csv", teacher_node)
            teacher_course_codes_csv_writer("teacher_course_codes.csv", teacher_node)
            teacher_rating_tags_csv_writer("teacher_rating_tags.csv", teacher_node)
            teacher_related_teachers_csv_writer("teacher_related_teachers.csv", teacher_node)
            #------------------------------------------------------------------
            break

          else:
            print(f"Received 'Professor not found' message for skipping inital request...")
            break


        except json.decoder.JSONDecodeError:
          print("Invalid JSON Response for Inital Request..skipping..")
          break
        #----------------------------------------------------------------

      else: # The response of the request failed, no data was returned
        print("GraphQL request failed with status code 1:", response.status_code)
        break

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the initial request retrying:", e)
        sleep(5)
        continue
    except PermissionError as pe:
      print(f"Did you open the file? Permission Error, retrying:", pe)
      sleep(5)
      continue


#========================



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
              print("=" *20 + f"COMPLETED WRITING TEACHER_ID: {teacher_node['id']} SPECIFIC TEACHER DATA" + "=" *20)
              break

          else:
            print(f"Received 'Professor not found' message for skipping 2nd request...")
            break

        except json.decoder.JSONDecodeError:
          print("Invalid JSON data response for second request..skipping")
          break

      else:
        print("GraphQL request failed with status code:", response.status_code)
        break

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the 2nd request retrying:", e)
        sleep(5)
        continue
    except PermissionError as pe:
      print(f"Did you open the file? Permission Error, retrying:", pe)
      sleep(5)
      continue

#----------------------------------------------------------------

# This code will only run when fetch_teacher_data.py is executed directly as a script
if __name__ == "__main__":
  fetch_teacher_data("VGVhY2hlci0yMTg0MzUw", "")  #fetch_teacher_data(teacher_id, cursor)


