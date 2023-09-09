# *****************************************************************************
# File: school_id_setup.py
# Author: Robert Boggs II
# Date: August 22, 2023
# Description: This script fetches school IDs from RateMyProfessors and writes them all into a text file.
# *****************************************************************************

# Fetches the following School Data:

# School ID:   
               
import requests # Used to make HTTP requests
import base64 # used to decode School ID

def fetch_school_id_list():
    # Define the GraphQL endpoint URL
    graphql_url = "https://www.ratemyprofessors.com/graphql"

    # Define the GraphQL request payload (I looked at the network request payload for graphql to find this)
    #This query will only request school's id
    payload = {
    "query": """
    query SchoolSearchResultsPageQuery(
      $query: SchoolSearchQuery!
      $count: Int!
      $cursor: String
    ) {
      search: newSearch {
        ...SchoolSearchPagination_search_1ZLmLD
      }
    }

    fragment SchoolSearchPagination_search_1ZLmLD on newSearch {
      schools(query: $query, first: $count, after: $cursor) {
        edges {
          cursor
          node {
            id
          }
        }
        pageInfo {
          hasNextPage
          endCursor
        }
        resultCount
      }
    }
    """,
    "variables": {
        "query": {
            "text": "*"
        },
        "count": 90000,         # count is the number of school ids to retrieve
        "cursor": ""        # Set your cursor value here if needed
    }
    }

    # Set headers based on the provided information
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Authorization": "Basic dGVzdDp0ZXN0",
        "Cookie": "_ga=GA1.1.1667084848.1690933012; ...",  
        "Referer": "https://www.ratemyprofessors.com/search/schools?q=*"
    }

    school_count = 0 # School Count (Keeps track of count)

    # Open a file in a specific directory for appending
    file_path = 'fetch_school_folder\\school_id_list.txt'   
    with open(file_path, 'w') as file: # write" mode ('w'). 
                                      #Allows you to create, modify or overwrite the content of the file
                                      

        while True: # Enter a loop to fetch School Ids until no next page is reached

            response = requests.post(graphql_url, json=payload, headers=headers) #Using the defined parameters from earlier

            # Check if the request was successful (status code 200) # if 200 we actually got a response with data back.
            if response.status_code == 200:
            
                data = response.json() #Get the data from the response of the request
                # print(data) #print raw data (debug purpose)

                school_node = data["data"]["search"]['schools']['edges'] #Get the node that has the school's list

                # Loop through the list of schools to extract information
                for school_entry in school_node:  # For every school entry in the list

                    school_node = school_entry['node']   #Get the node that has the school's specific data
                    school_count += 1 # increment school count

                    school_id = school_node['id'] # Get the school's specific ID

                    # decoded_bytes = base64.b64decode(school_id)
                    # school_id = decoded_bytes.decode('utf-8')

                    file.write(school_id + '\n') #append School ID to the file
                    # print(school_id) #Optional debug print

                #Is there a next page? boolean
                has_next_page = data['data']['search']['schools']['pageInfo']['hasNextPage']

                if has_next_page: #Check if there is a next page if so update cursor position to only get new data.
                    cursor = data['data']['search']['schools']['pageInfo']['endCursor'] # Get the current position of the cursor
                    payload['variables']['cursor'] = cursor #Update payload cursor here
                
                else:
                    # print(school_count)
                    print("=" *20 + "COMPLETED WRITING SCHOOL IDs" + "=" *20)
                    break  # Exit the loop if there's no next page

            else:
                print("GraphQL request failed with status code:", response.status_code)
                break # Exit the loop on error

#------------------------------------------------------------------------------------------

# This code will only run when school_id_setup.py is executed directly as a script
if __name__ == "__main__":

  fetch_school_id_list()

    

