# *****************************************************************************
# File: examples.py
# Author: Robert Boggs II
# Date: September 3, 2023
# Description: This shows various examples on how to use the functions below:
    # teacher_id_setup()
    # fetch_teacher_data(teacher_id, cursor)
    # fetch_all_teacher_data()

    # school_id_setup()
    # fetch_school_data(school_id, cursor)
    # fetch_all_school_data()
# *****************************************************************************

import sys
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Inserts fetch_school_folder into the python search path
sys.path.insert(1, f'{current_dir}/fetch_school_folder')
# Inserts fetch_teacher_folder into the python search path
sys.path.insert(2, f'{current_dir}/fetch_teacher_folder')

#----School Imports from /fetch_school_folder
import school_id_setup 
import fetch_school_data
import fetch_all_school_data
#-----

#-----Teacher Imports from /fetch_teacher_folder
import teacher_id_setup
import fetch_teacher_data
import fetch_all_teacher_data
#-----

# EXAMPLES FOR REQUESTING TEACHER DATA
#================================================================

# Get Teacher IDs List:
# Writes to a file in /fetch_teacher_folder it will write as "teacher_id_list.txt"

#================================================================
# teacher_id_setup.fetch_teacher_id_list()
#================================================================

#----------------------------------------------------------------

# Fetch Teacher Data (Specific Teacher)
# This will fetch:
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

#                Teacher's Course Codes: (For Course Codes)
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
# 
# #              Rating: (For x Ratings)
#----------------------------------------------------------------
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
#============================================================================
#fetch_teacher_data.fetch_teacher_data("VGVhY2hlci0yMTg0MzUw", "")  #fetch_teacher_data(teacher_id, cursor)
#============================================================================
#---------------------------------------------------------------------------

# Fetch All Teacher Data (All Teachers)
# This will fetch everything in the base fetch_teacher_data because its just looping through the teacher_id_list for each teacher id

# The current setup asks if you would like to continue after printing all the data for the specific teacher

#================================================================
# fetch_all_teacher_data.fetch_all_teacher_data()
#================================================================




# EXAMPLES FOR REQUESTING SCHOOL DATA
#================================================================

# Get School IDs List:
# Writes to a file in /fetch_school_folder it will write as "school_id_list.txt"

#================================================================
# school_id_setup.fetch_school_id_list()
#================================================================

#----------------------------------------------------------------
# Fetch School Data (Specific School)
# This will fetch:

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
# 
# #                    Rating: (For x Ratings)
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

#                    Thumb: (For x Thumbs)
# computerId:                      
# id:                               
# thumbsDown:                      
# thumbsUp:
# 
    
#================================================================
# fetch_school_data.fetch_school_data("U2Nob29sLTU2Nw==", "") #fetch_school_data(school_id, cursor)
#================================================================

# Fetch All School Data (All Schools)
# This will fetch everything in the base fetch_school_data because its just looping through the school_id_list for each school id

# The current setup asks if you would like to continue after printing all the data for the specific school

#================================================================
# fetch_all_school_data.fetch_all_school_data()
#================================================================





