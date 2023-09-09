# *****************************************************************************
# File: school_rating_payload.py
# Author: Robert Boggs II
# Date: August 22, 2023
# Description: This is a payload for fetch_school_data.py to fetch school data from RateMyProfessors.
# *****************************************************************************

# This payload will run until all ratings have been fetched when used by fetch_school_data.py

#----------------------------------------------------------------
# school_id: the specific school id, used to get the specific school's ratings
# rating_count: This is the number of ratings you wish to fetch per request
# cursor: position to start fetching NOTE: "" is the beginning
#----------------------------------------------------------------

def generate_school_rating_query_payload(school_id  : str, ratings_amount_per_request : int, cursor : str):

 #This query only returns:

#                    Rating:
# --typename:                        
# id:                              
# legacyId:                        
# date:                     
# createdByUser:                  
# reputationRating:                
# foodRating:                      
# locationRating:                  
# clubsRating:                     
# opportunitiesRating:             
# socialRating:                    
# facilitiesRating:                
# happinessRating:                 
# internetRating:                  
# safetyRating:                    
# comment:                         
# flagStatus:                      
# Thumbs Down Total:                
# Thumbs Up Total:                  

#                    Thumb: (For Thumbs)
# computerId:                      
# id:                               
# thumbsDown:                      
# thumbsUp:
# 
# 
#                      Page Info:
# endCursor
# hasNextPage

  query_string = f"""
    query SchoolRatingsPageQuery($id: ID!, $cursor: String) {{
      school: node(id: $id) {{
        __typename
        ... on School {{
          id
          ...SchoolRatingsContainer_school
        }}
        id
      }}
    }}
       
    fragment SchoolRatingsContainer_school on School {{
      ...SchoolRatingsList_school
    }}
    
    fragment SchoolRatingsList_school on School {{
      id
      ratings(first: {ratings_amount_per_request}, after: $cursor) {{
        edges {{
          cursor
          node {{
            ...SchoolRating_rating
            id
            __typename
          }}
        }}
        pageInfo {{
          hasNextPage
          endCursor
        }}
      }}
      ...SchoolRating_school
    }}
    
    fragment SchoolRating_rating on SchoolRating {{
      clubsRating
      comment
      date
      facilitiesRating
      foodRating
      happinessRating
      internetRating
      locationRating
      opportunitiesRating
      reputationRating
      safetyRating
      socialRating
      legacyId
      flagStatus
      createdByUser
      ...SchoolRatingFooter_rating
    }}
    
    fragment SchoolRating_school on School {{
      ...SchoolRatingSuperHeader_school
      ...SchoolRatingFooter_school
    }}
    
    fragment SchoolRatingSuperHeader_school on School {{
      name
      legacyId
    }}
    
    fragment SchoolRatingFooter_school on School {{
      id
      legacyId
      ...Thumbs_school
    }}
    
    fragment Thumbs_school on School {{
      id
      legacyId
    }}
    
    fragment SchoolRatingFooter_rating on SchoolRating {{
      id
      comment
      flagStatus
      legacyId
      ...Thumbs_schoolRating
    }}
    
    fragment Thumbs_schoolRating on SchoolRating {{
      id
      legacyId
      thumbsDownTotal
      thumbsUpTotal
      userThumbs {{
        computerId
        thumbsUp
        thumbsDown
        id
      }}
    }}
    
  """

  payload = {
      "query": query_string, # query of the request
      "variables": {
          "id": school_id, #school id to retrieve that school's data
          "cursor": cursor #position to start cursor
      }
  }

  return payload