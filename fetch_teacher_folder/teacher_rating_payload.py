# *****************************************************************************
# File: teacher_rating_payload.py
# Author: Robert Boggs II
# Date: August 22, 2023
# Description: This is a payload for fetch_teacher_data.py to fetch teacher data from RateMyProfessors.
# *****************************************************************************

#----------------------------------------------------------------
# teacher_id: the specific teacher id, used to get the specific teacher's ratings
# rating_count: This is the number of ratings you wish to fetch per request
# cursor: position to start fetching NOTE: "" is the beginning
#----------------------------------------------------------------

def generate_teacher_rating_payload(teacher_id: str, cursor: str):
    
  # This query will return:

#              Rating:
# __typename:                        
# id:                               
# legacyId:                        
# class:                            
# date:                      
# adminReviewedAt:                
# createdByUser:                  
# clarityRating (Quality):                          
# difficultyRating:                
# isForCredit:                       
# attendanceMandatory:                      
# wouldTakeAgain:                 
# grade:                            
# textbookUse:                         
# isForOnlineClass:                     
# comment:                                                     
# helpfulRating:                   
# ratingTags:                      
# flagStatus:                      
# teacherNote:                     
# thumbsDownTotal:                
# thumbsUpTotal:                  
#                    Thumb: (For x Thumbs)
# computerId:                      
# Id:                               
# thumbsDown:                      
# thumbsUp:
# 
#                 Page Info
# hasNextPage
# cursor                        

  query_string = f"""
  query TeacherRatingsPageQuery($id: ID!, $cursor: String) {{
  node(id: $id) {{
    __typename
    ... on Teacher {{
      id
      ratings(first: 200, after: $cursor) {{           # Get This many ratings
        edges {{
          cursor
          node {{
            ...Rating_rating
            id
            __typename
          }}
        }}
        pageInfo {{
          hasNextPage
          endCursor
        }}
      }}
    }}
  }}
}}
fragment Rating_rating on Rating {{
  id
  comment
  flagStatus
  createdByUser
  ...RatingHeader_rating
  ...RatingSuperHeader_rating
  ...RatingValues_rating
  ...CourseMeta_rating
  ...RatingTags_rating
  ...RatingFooter_rating
  ...ProfessorNoteSection_rating
}}
fragment RatingHeader_rating on Rating {{
  legacyId
  date
  class
  helpfulRating
  clarityRating
  isForOnlineClass
}}
fragment RatingSuperHeader_rating on Rating {{
  legacyId
}}
fragment RatingValues_rating on Rating {{
  helpfulRating
  clarityRating
  difficultyRating
}}
fragment CourseMeta_rating on Rating {{
  attendanceMandatory
  wouldTakeAgain
  grade
  textbookUse
  isForOnlineClass
  isForCredit
}}
fragment RatingTags_rating on Rating {{
  ratingTags
}}
fragment RatingFooter_rating on Rating {{
  id
  comment
  adminReviewedAt
  flagStatus
  legacyId
  thumbsUpTotal
  thumbsDownTotal
  thumbs {{
    thumbsUp
    thumbsDown
    computerId
    id
  }}
  teacherNote {{
    id
  }}
}}
fragment ProfessorNoteSection_rating on Rating {{
  teacherNote {{
    ...ProfessorNote_note
    id
  }}
  ...ProfessorNoteEditor_rating
}}
fragment ProfessorNote_note on TeacherNotes {{
  comment
  ...ProfessorNoteHeader_note
  ...ProfessorNoteFooter_note
}}
fragment ProfessorNoteEditor_rating on Rating {{
  id
  legacyId
  class
  teacherNote {{
    id
    teacherId
    comment
  }}
}}
fragment ProfessorNoteHeader_note on TeacherNotes {{
  createdAt
  updatedAt
}}
fragment ProfessorNoteFooter_note on TeacherNotes {{
  legacyId
  flagStatus
}}
"""
    
  payload = {
      "query": query_string,
      "variables": {
          "id": teacher_id,
          "cursor": cursor #position to start cursor
      }
  }
  return payload



  