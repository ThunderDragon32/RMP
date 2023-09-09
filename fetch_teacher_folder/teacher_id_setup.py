# *****************************************************************************
# File: teacher_id_setup.py
# Author: Robert Boggs II
# Date: August 22, 2023
# Description: This script fetches teacher IDs from RateMyProfessors and writes them all into a text file.
# *****************************************************************************

# Fetches the following Teacher Data:

# Teacher ID:   
               
import requests # Used to make HTTP requests
import base64 # used to decode Teacher ID

def fetch_teacher_id_list():

    # Define the GraphQL endpoint URL
    graphql_url = "https://www.ratemyprofessors.com/graphql"

    # Define the GraphQL request payload (I looked at the network request payload for graphql to find this)
    #This query will only request teacher's id
    payload = {
        "query": """
        query TeacherSearchPaginationQuery(
        $count: Int!
        $cursor: String
        $query: TeacherSearchQuery!
        ) {
        search: newSearch {
            ...TeacherSearchPagination_search_1jWD3d
        }
        }
    
        fragment TeacherSearchPagination_search_1jWD3d on newSearch {
        teachers(query: $query, first: $count, after: $cursor) {
            didFallback
            edges {
            cursor
            node {
                id
                __typename
            }
            }
            pageInfo {
            hasNextPage
            endCursor
            }
            resultCount
            filters {
            field
            options {
                value
                id
            }
            }
        }
        }

        """,
        "variables": {
            "count": 90000, # Number of Teacher's ID to fetch 90k at once seems to be the max
            "cursor": "",  # Position of cursor (Position to start fetching) ("" = start)
            "query": {
                "text": "",
                "schoolID": "",
                "fallback": True,
                "departmentID": None
            }
        }
    }
    
    

    # Set headers based on the provided information
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Authorization": "Basic dGVzdDp0ZXN0",
        "Cookie": "_ga=GA1.1.1667084848.1690933012; ...",  
        "Referer": "https://www.ratemyprofessors.com/search/professors?q=*"
    }

    teacherNumber = 0 # Teacher Count (Keeps track of count)
    # Open a file in a specific directory for appending
    file_path = 'fetch_teacher_folder\\teacher_id_list.txt'   
    with open(file_path, 'w') as file: # write" mode ('w'). 
                                      #Allows you to create, modify or overwrite the content of the file

        while True: # Enter a loop to fetch Teacher Ids until no next page is reached

            response = requests.post(graphql_url, json=payload, headers=headers)

            # Check if the request was successful (status code 200) # if 200 we actually got a response with data back.
            if response.status_code == 200:
            
                data = response.json()
                #print(data) #print raw data (debug purpose)

                # Access the 'teachers' list from the data
                teachers_list = data['data']['search']['teachers']['edges']

                # Loop through the list of teachers to extract information
                for teacher_entry in teachers_list:  # For every teacher entry in the list

                    teacher_node = teacher_entry['node']   #get the node from the teacher entry
                    teacherNumber += 1 # increment teacherNumber
                    teacher_id = teacher_node['id']

                    # decoded_bytes = base64.b64decode(teacher_id)
                    # teacher_id = decoded_bytes.decode('utf-8')

                    file.write(teacher_id + '\n') # append Teacher ID to file
                    #print(teacher_id) #optional debug print
                    #print(teacherNumber)
                #Is there a next page? boolean
                has_next_page = data['data']['search']['teachers']['pageInfo']['hasNextPage']

                if has_next_page: #Check if there is a next page if so update cursor position to only get new data.
                    cursor = data['data']['search']['teachers']['pageInfo']['endCursor'] # Get the current position of the cursor
                    payload['variables']['cursor'] = cursor #Update payload cursor here
                
                else:
                    print("=" *20 + "COMPLETED WRITING TEACHER IDs" + "=" *20)
                    break  # Exit the loop if there's no next page

            else:
                print("GraphQL request failed with status code:", response.status_code)
                break # Exit the loop on error

#------------------------------------------------------------------------------------------


# This code will only run when teacher_id_setup.py is executed directly as a script
if __name__ == "__main__":

    fetch_teacher_id_list()

    

