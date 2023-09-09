# *****************************************************************************
# File: teacher_inital_payload.py
# Author: Robert Boggs II
# Date: August 22, 2023
# Description: This is a payload for fetch_teacher_data.py to fetch teacher data from RateMyProfessors.
# *****************************************************************************

#----------------------------------------------------------------
# Takes teacher_id to get the specific teacher's data
#----------------------------------------------------------------

def generate_inital_payload(teacher_id : str):
    
# This query will return:

#                       Teacher
# --------------------------------------------------
# __typename:                        
# id:                       
# legacyId:                        
# firstName:                       
# lastName:                        
# departmentId:                    
# department:                       
# avgDifficulty:               
# avgRating:                   
# numRatings:                
# wouldTakeAgainPercent:         
# isProfCurrentUser:        
# isSaved:                         
# lockStatus:                      

#                Teacher's School:
# --------------------------------------------------
# id:                               
# legacyId:                        
# name:                             
# country:                        
# state:
# city:
# avgRating:                   
# numRatings:                

#                Teacher's Rating Distribution:
# --------------------------------------------------
# r5 (Awesome):                          
# r4 (Great):                            
# r3 (Good):                             
# r2 (OK):                               
# r1 (Awful):                            

#                Teacher's Course Codes: (For x Course Codes)
# --------------------------------------------------
# courseName:                    
# courseCount:                   

#                Teacher Rating Tags: (For x Tags)
# --------------------------------------------------
# id:                         
# legacyId:                      
# tagName:                     


#                Teacher's Related Teachers: (For x Related Teachers)
# --------------------------------------------------
# id:                             
# legacyId:                      
# firstName:                     
# lastName:                      
# avgRating:                 

#                 Page Info
#hasNextPage
# cursor

    inital_payload = {
  "query": """
query TeacherRatingsPageQuery  ($id: ID!) {  
node(id: $id) {    
__typename    
... on Teacher {      
id      
legacyId      
firstName      
lastName      
department      
school {        
legacyId        
name        
city        
state        
country        
id  
}      
lockStatus      
...StickyHeader_teacher      
...RatingDistributionWrapper_teacher      
...TeacherInfo_teacher      
...SimilarProfessors_teacher      
...TeacherRatingTabs_teacher    
}    
id  
}
}
fragment StickyHeader_teacher on Teacher {
  ...HeaderDescription_teacher
  ...HeaderRateButton_teacher
}

fragment RatingDistributionWrapper_teacher on Teacher {
  ...NoRatingsArea_teacher
  ratingsDistribution {    
total    
...RatingDistributionChart_ratingsDistribution  
}
}
fragment TeacherInfo_teacher on Teacher {
  id
  lastName
  numRatings
  ...RatingValue_teacher
  ...NameTitle_teacher
  ...TeacherTags_teacher
  ...NameLink_teacher
  ...TeacherFeedback_teacher
  ...RateTeacherLink_teacher
}
fragment SimilarProfessors_teacher on Teacher {
  department
  relatedTeachers {
    legacyId
    ...SimilarProfessorListItem_teacher
    id
  }
}
fragment TeacherRatingTabs_teacher on Teacher {
  numRatings
  courseCodes {
    courseName
    courseCount
  }
  ...RatingsList_teacher
  ...RatingsFilter_teacher
}
fragment RatingsList_teacher on Teacher {
  id
  legacyId
  lastName
  numRatings
  school {
    id
    legacyId
    name
    city
    state
    avgRating
    numRatings
  }
  ...Rating_teacher
  ...NoRatingsArea_teacher
  ratings(first: 0) {           #Get This many rating
    edges {
      cursor
      node {
        ...Rating_rating
        id
        __typename
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
fragment RatingsFilter_teacher on Teacher {
  courseCodes {
    courseCount
    courseName
  }
}
fragment Rating_teacher on Teacher {
  ...RatingFooter_teacher
  ...RatingSuperHeader_teacher
  ...ProfessorNoteSection_teacher
}
fragment NoRatingsArea_teacher on Teacher {
  lastName
  ...RateTeacherLink_teacher
}
fragment Rating_rating on Rating {
  comment
  flagStatus
  createdByUser
  teacherNote {
    id
  }
  ...RatingHeader_rating
  ...RatingSuperHeader_rating
  ...RatingValues_rating
  ...CourseMeta_rating
  ...RatingTags_rating
  ...RatingFooter_rating
  ...ProfessorNoteSection_rating
}
fragment RatingHeader_rating on Rating {
  legacyId
  date
  class
  helpfulRating
  clarityRating
  isForOnlineClass
}
fragment RatingSuperHeader_rating on Rating {
  legacyId
}
fragment RatingValues_rating on Rating {
  helpfulRating
  clarityRating
  difficultyRating
}
fragment CourseMeta_rating on Rating {
  attendanceMandatory
  wouldTakeAgain
  grade
  textbookUse
  isForOnlineClass
  isForCredit
}
fragment RatingTags_rating on Rating {
  ratingTags
}
fragment RatingFooter_rating on Rating {
  id
  comment
  adminReviewedAt
  flagStatus
  legacyId
  thumbsUpTotal
  thumbsDownTotal
  thumbs {
    thumbsUp
    thumbsDown
    computerId
    id
  }
  teacherNote {
    id
  }
}
fragment ProfessorNoteSection_rating on Rating {
  teacherNote {
    ...ProfessorNote_note
    id
  }
  ...ProfessorNoteEditor_rating
}
fragment ProfessorNote_note on TeacherNotes {
  comment
  ...ProfessorNoteHeader_note
  ...ProfessorNoteFooter_note
}
fragment ProfessorNoteEditor_rating on Rating {
  id
  legacyId
  class
  teacherNote {
    id
    teacherId
    comment
  }
}
fragment ProfessorNoteHeader_note on TeacherNotes {
  createdAt
  updatedAt
}
fragment ProfessorNoteFooter_note on TeacherNotes {
  legacyId
  flagStatus
}
fragment RateTeacherLink_teacher on Teacher {
  legacyId
  numRatings
  lockStatus
}
fragment RatingFooter_teacher on Teacher {
  id
  legacyId
  lockStatus
  isProfCurrentUser
}
fragment RatingSuperHeader_teacher on Teacher {
  firstName
  lastName
  legacyId
  school {
    name
    id
  }
}
fragment ProfessorNoteSection_teacher on Teacher {
  ...ProfessorNote_teacher
  ...ProfessorNoteEditor_teacher
}
fragment ProfessorNote_teacher on Teacher {
  ...ProfessorNoteHeader_teacher
  ...ProfessorNoteFooter_teacher
}
fragment ProfessorNoteEditor_teacher on Teacher {
  id
}
fragment ProfessorNoteHeader_teacher on Teacher {
  lastName
}
fragment ProfessorNoteFooter_teacher on Teacher {
  legacyId
  isProfCurrentUser
}
fragment SimilarProfessorListItem_teacher on RelatedTeacher {
  legacyId
  firstName
  lastName
  avgRating
}
fragment RatingValue_teacher on Teacher {
  avgRating
  numRatings
  ...NumRatingsLink_teacher
}
fragment NameTitle_teacher on Teacher {
  id
  firstName
  lastName
  department
  school {
    legacyId
    name
    id
  }
  ...TeacherDepartment_teacher
  ...TeacherBookmark_teacher
}
fragment TeacherTags_teacher on Teacher {
  lastName
  teacherRatingTags {
    legacyId
    tagCount
    tagName
    id
  }
}
fragment NameLink_teacher on Teacher {
  isProfCurrentUser
  id
  legacyId
  firstName
  lastName
  school {
    name
    id
  }
}
fragment TeacherFeedback_teacher on Teacher {
  numRatings
  avgDifficulty
  wouldTakeAgainPercent
}
fragment TeacherDepartment_teacher on Teacher {
  department
  departmentId
  school {
    legacyId
    name
    id
  }
}
fragment TeacherBookmark_teacher on Teacher {
  id
  isSaved
}
fragment NumRatingsLink_teacher on Teacher {
  numRatings
  ...RateTeacherLink_teacher
}
fragment RatingDistributionChart_ratingsDistribution on ratingsDistribution {
  r1
  r2
  r3
  r4
  r5
}
fragment HeaderDescription_teacher on Teacher {
  id
  firstName
  lastName
  department
  school {
    legacyId
    name
    city
    state
    id
  }
  ...TeacherTitles_teacher
  ...TeacherBookmark_teacher
}
fragment HeaderRateButton_teacher on Teacher {
  ...RateTeacherLink_teacher
}
fragment TeacherTitles_teacher on Teacher {
  department
  school {
    legacyId
    name
    id
  }
}
"""
,
"variables":
# {"id":"VGVhY2hlci0yMTg0MzUw",
{"id": teacher_id,
}
    }

    return inital_payload