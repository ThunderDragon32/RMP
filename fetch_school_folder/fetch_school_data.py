# *****************************************************************************
# File: fetch_school_data.py
# Author: Robert Boggs II 
# Date: August 22, 2023
# Description: This script fetches School data from RateMyProfessors.
# *****************************************************************************
import json
from time import sleep
import requests # Used to make HTTP requests
import base64 # Used to decode IDs
from school_rating_payload import generate_school_rating_query_payload # import the rating payload function
from school_inital_payload import generate_inital_payload # import the inital payload function
from school_print_functions import * # Simply imports all print functions from school_print_functions.py used to display the school data
from school_csv_functions import * # Simply imports all csv functions from school_csv_functions.py used

class Color:
    RED = '\033[31m'
    GREEN = '\033[32m'
    RESET = '\033[0m'

def fetch_school_data(school_id : str, cursor : str):

    # Define the GraphQL endpoint URL
    graphql_url = "https://www.ratemyprofessors.com/graphql" 

    # Header set based on given information from requests made on the site for graphql
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Authorization": "Basic dGVzdDp0ZXN0",
        "Cookie": "_ga=GA1.1.1667084848.1690933012; ...",  
        "Referer": "https://www.ratemyprofessors.com/search/schools?q=*"
    }
#=====Inital Request (School's Basic Data)

    inital_payload = generate_inital_payload(school_id) ##Give payload the School ID to collect data from the School

    while True:
        try:
            # Send the GraphQL request 
            # graph_url is the endpoint url,
            # json=inital_payload is generate_inital_payload(school_id)
            #headers is set to header (we defined earlier)
            response = requests.post(graphql_url, json=inital_payload, headers=headers)

            # Check if the request was successful (status code 200), this checks to see if we actually got a response back.
            if response.status_code == 200:
                try:
                    data = response.json() #Get the data from the response of the request
                    # print(data) #Debug print
                    school_node = data["data"]["school"] # Get the School node this holds the data we want.
        
                    if school_node:
                        # print(school_node)

                        # Print functions to print data to the console
                        #--------------------------------------------------------------
                        # print_school(school_node) 
                        # print_school_rating_distribution(school_node)
                        #------------------------------------------------

                        # CSV Writer Functions to write data to a CSV file
                        #----------------------------------------------------------------
                        school_csv_writer("school.csv", school_node)
                        school_rating_distribution_csv_writer("school_rating_distribution.csv", school_node)
                        #--------------------------------------------------------------
                        break

                    else:
                        print(f"{Color.RED}Received 'School not found' message for {school_id} skipping inital request...\n{data}{Color.RESET}")
                        break

                except json.decoder.JSONDecodeError:
                    print(f"{Color.RED}Invalid JSON response for inital request..skipping{Color.RESET}")
                    break

            else: # The response of the request failed, no data was returned
                print(f"{Color.RED}GraphQL request failed with status code:{Color.RESET}", response.status_code)
                break

        except requests.exceptions.RequestException as e:
            print(f"{Color.RED} An error occurred during the initial request retrying:{Color.RESET}", e)
            sleep(5)
            continue

        except PermissionError as pe:
            print(f"{Color.RED} Did you open the file? Permission Error, retrying:{Color.RESET}", pe)
            sleep(5)
            continue

#=====Second Request (All School's Specific Ratings)
    while True: #While there are more ratings available (if has_next_page)
        try:
            rating_payload = generate_school_rating_query_payload(school_id, cursor) #generate_school_rating_query_payload(school_id, cursor): NOTE: cursor = "" is BEGINNING
        
            # Send the GraphQL request
            response = requests.post(graphql_url, json=rating_payload, headers=headers)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                try:
                    data = response.json()
                    school_node = data['data']['school'] # Grab school_node to access data

                    if school_node:
            
                        # Print functions to print data to the console
                        #--------------------------------------------------------------
                        # print_school_individual_ratings(school_node)
                        #--------------------------------------------------------------

                        # CSV Writer Functions to write data to a CSV file
                        #----------------------------------------------------------------
                        school_individual_ratings_csv_writer("school_student_ratings.csv", school_node)
                        #----------------------------------------------------------------
                    
                        has_next_page = school_node['ratings']['pageInfo']['hasNextPage'] # If next page True otherwise False
                        if has_next_page:
                            # print(school_node['ratings']['pageInfo']['endCursor'])
                            cursor = school_node['ratings']['pageInfo']['endCursor'] # Get the new cursor postion
            
                        else: # No more ratings BREAK OUT of While Loop
                            print("=" *20 + f"COMPLETED WRITING SCHOOL_ID: {school_node['id']} SPECIFIC SCHOOL DATA" + "=" *20)
                            break

                    else:
                        print(f"{Color.RED}Received 'School not found' message for {school_id} skipping 2nd request...\n{data}{Color.RESET}")
                        break

                except json.decoder.JSONDecodeError:
                    print(f"{Color.RED}Invalid JSON data response for second request..skipping{Color.RESET}")
                    break
           
            else:
                print("GraphQL request failed with status code:", response.status_code)
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

# This code will only run when fetch_school_data.py is executed directly as a script
if __name__ == "__main__":
    fetch_school_data("U2Nob29sLTM=", "")
