# *****************************************************************************
# File: school_inital_payload.py
# Author: Robert Boggs II
# Date: August 22, 2023
# Description: This is a payload for fetch_school_data.py to fetch school data from RateMyProfessors.
# *****************************************************************************

#This payload will ONLY run once per school to get the inital data of the school when used by fetch_school_data.py

#----------------------------------------------------------------
# Takes school_id to get the specific school's data
#----------------------------------------------------------------



def generate_inital_payload(school_id : str):
    
  #  #This query only returns:

#                    School
# --------------------------------------------------
# __typename:                      
# id:                      
# legacyId:                       
# name:                  
# city:
# state:
# country:                       
# numRatings:            
# avgRating:                  
# avgRatingRounded:      

#        School's Rating Distribution:
# --------------------------------------------------
# campusCondition:                
# campusLocation:                 
# careerOpportunities:            
# clubAndEventActivities:     
# foodQuality:                    
# internetSpeed:                  
# schoolReputation:               
# schoolSafety:                   
# schoolSatisfaction:             
# socialActivities:                     

    inital_payload = {
        "query": """
        query SchoolRatingsPageQuery($id: ID!) {
          school: node(id: $id) {
            __typename
            ... on School {
              id
              legacyId
              name
              city
              state
              country
              numRatings
              ...StickyHeader_school
              ...OverallRating_school
              ...SchoolSummary_school
            }
            id
          }
        }
        
        fragment StickyHeader_school on School {
          ...HeaderDescription_school
          ...HeaderRateButton_school
        }
        
        fragment OverallRating_school on School {
          avgRatingRounded
          avgRating
          numRatings
        }
        
        fragment SchoolSummary_school on School {
          summary {
            schoolReputation
            schoolSatisfaction
            internetSpeed
            campusCondition
            schoolSafety
            careerOpportunities
            socialActivities
            foodQuality
            clubAndEventActivities
            campusLocation
          }
        }
        
        fragment HeaderDescription_school on School {
          name
          city
          state
          legacyId
        }
        
        fragment HeaderRateButton_school on School {
          ...RateSchoolLink_school
          ...CompareSchoolLink_school
        }
        
        fragment RateSchoolLink_school on School {
          legacyId
        }
        
        fragment CompareSchoolLink_school on School {
          legacyId
        }
        """,
        "variables": {
            "id": school_id
        }
    }

    return inital_payload
