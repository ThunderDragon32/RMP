# *****************************************************************************
# File: teacher_csv_functions.py
# Author: Robert Boggs II 
# Date: September 7, 2023
# Description: Functions to write teacher data into a CSV file
# *****************************************************************************  
import os
import csv
import html
import threading

#Thread locks to ensure only one thread can write to a file at a time
teacher_lock = threading.Lock()
teacher_course_codes_lock = threading.Lock()
teacher_rating_tags_lock = threading.Lock()
teacher_related_teachers_lock = threading.Lock()
student_ratings_lock = threading.Lock()
teacher_rating_thumbs_lock = threading.Lock()
#-------------------------------------------------------------------


# Used To write data into CSV (This is called in each function below)
def csv_writer(file_name, header_row, data_row, lock):
  with lock:

    # This is used later as a check to see if the header is present already
    file_exists = os.path.isfile(file_name) and os.path.getsize(file_name) > 0
    #------

    with open(file_name, mode='a', newline='', encoding='utf-8') as csv_file:
      csv_writer = csv.writer(csv_file)

      if not file_exists: # Writes the header to the file if its not already present
        csv_writer.writerow(header_row)

      csv_writer.writerow(data_row) # Write the data

#--------------------------------------------------------------------


def teacher_csv_writer(file_name: str, teacher_node: dict):
    
  # 20 Total Values ----------------------------------------------------
  header_row = ["Type Name", "Teacher ID", "Teacher Legacy ID", "First Name", 
                  "Last Name", "Department ID", "Department", "Average Difficulty", 
                  "Average Rating", "Number of Ratings", "Would Take Again Percent", 
                  "Is Professor Current User", "Is Saved", "Lock Status", "School ID",
                    "Awesome", "Great", "Good", "OK", "Awful"]
  #------------------------------------------------------------------------


  data_row = [teacher_node['__typename'], teacher_node['id'],teacher_node['legacyId'], 
                teacher_node['firstName'],teacher_node['lastName'], teacher_node['departmentId'],
                  teacher_node['department'], teacher_node['avgDifficulty'], teacher_node['avgRating'],  
                  teacher_node['numRatings'], teacher_node['wouldTakeAgainPercent'], teacher_node['isProfCurrentUser'],
                     teacher_node['isSaved'], teacher_node['lockStatus'], teacher_node['school']['id'], 
                     teacher_node['ratingsDistribution']['r5'], teacher_node['ratingsDistribution']['r4'], teacher_node['ratingsDistribution']['r3'],
                        teacher_node['ratingsDistribution']['r2'], teacher_node['ratingsDistribution']['r1']]
    

  # Writes the data into the CSV file
  csv_writer(file_name, header_row, data_row, teacher_lock)
  #---------------------------------




def teacher_course_codes_csv_writer(file_name : str, teacher_node: dict):

  # 3 Total Values
  header_row = ["Teacher ID", "Course Name", "Course Count"]
  #----------------------------------------------------------------

  for number, course in enumerate(teacher_node['courseCodes'], start=1): # For every course in teacher_node['courseCodes']
    data_row = [teacher_node['id'], course['courseName'], course['courseCount']] # Get the values     
    csv_writer(file_name, header_row, data_row, teacher_course_codes_lock) # write the data to the CSV


     
def teacher_rating_tags_csv_writer(file_name : str, teacher_node: dict):

  # 4 Total Values
  header_row = ["Teacher ID", "Tag ID", "Tag Legacy ID", "Tag Name"]
  #----------------------------------------------------------------

  for number, tag in enumerate(teacher_node['teacherRatingTags'], start = 1): # For every tag in teacher_node['teacherRatingTags']
    data_row = [teacher_node['id'], tag['id'], tag['legacyId'], tag['tagName']] # get the values
    csv_writer(file_name, header_row, data_row, teacher_rating_tags_lock) # Write the data to the CSV



def teacher_related_teachers_csv_writer(file_name : str, teacher_node: dict):

  # 6 Total Values --------------------------------
  header_row = ["Teacher ID", "Related Teacher ID", "Related Teacher ID", "First Name", "Last Name", "Average Rating"]
  #----------------------------------------------------------------

  for number, teacher in enumerate(teacher_node['relatedTeachers'], start = 1): # For every teacher in teacher_node['relatedTeachers']
    data_row = [teacher_node['id'], teacher['id'], teacher['legacyId'], teacher['firstName'], teacher['lastName'], teacher['avgRating']] # Get the values
    csv_writer(file_name, header_row, data_row, teacher_related_teachers_lock) # Write the data to the CSV



def student_ratings_csv_writer(file_name: str, teacher_node: dict):

  # 21 Total Values -------------------------------
  header_row = ["Teacher ID", "Type Name", "Rating ID", "Rating Legacy ID", "Class", "Date Posted", "Admin Reviewed At",
                 "Created By User", "Quality", "Difficulty", "For Credit", "Attendance", "Would Take Again",
                 "Grade", "Textbook", "Online Class", "Comment", "Flag Status", "Teacher Note", "Thumbs Down Total", "Thumbs Up Total"]
  #------------------------------------------------

  ratings_edges = teacher_node['ratings']['edges']

  for number, edge in enumerate(ratings_edges, start=1): #For every edge (To get each specific rating)
    rating_node = edge['node']

    # These are used to clean the data up a bit
    text_book_use = rating_node['textbookUse']
    if text_book_use is not None and isinstance(text_book_use, int):
      text_book_use = "False" if text_book_use < 3 else "True"
    else:
      text_book_use = ""  

    would_take_again = rating_node['wouldTakeAgain']
    if would_take_again is not None and isinstance(would_take_again, int):
      would_take_again = "False" if would_take_again == 0 else "True"
    else:
      would_take_again = ""  

    attendanceMandatory = rating_node['attendanceMandatory']
    if attendanceMandatory is not None and isinstance(attendanceMandatory, str):
      if attendanceMandatory == "Y" or attendanceMandatory == "N" or attendanceMandatory == "mandatory":
        attendanceMandatory = "True" 
      elif attendanceMandatory == "non mandatory":
        attendanceMandatory = "False"
    else:
      attendanceMandatory = ""

    #------------------------------------------


    data_row = [teacher_node['id'], rating_node['__typename'], rating_node['id'], 
                rating_node['legacyId'], rating_node['class'], rating_node['date'], 
                rating_node['adminReviewedAt'], rating_node['createdByUser'], 
                rating_node['clarityRating'], rating_node['difficultyRating'],
                rating_node['isForCredit'], attendanceMandatory,
                would_take_again, rating_node['grade'], text_book_use,
                rating_node['isForOnlineClass'], html.unescape(rating_node['comment']),
                rating_node['flagStatus'], rating_node['teacherNote'], rating_node['thumbsDownTotal'],
                rating_node['thumbsUpTotal']] 

    
    csv_writer(file_name, header_row, data_row, student_ratings_lock) # Write the data to the CSV file


def teacher_rating_thumbs_csv_writer(file_name : str, teacher_node : dict):

  # 6 Total Values
  header_row = ["Teacher ID", "Rating ID", "Computer ID", "Thumb ID", "Thumb Down", "Thumb Up"]
  #----------------------------------------------------------------
  ratings_edges = teacher_node['ratings']['edges']

  for number, edge in enumerate(ratings_edges, start=1): # For every edge in ratings_edge (For every rating)
    rating_node = edge['node']

    for number, thumbs in enumerate(rating_node['thumbs'], start=1): # For every thumb in rating

      data_row = [teacher_node['id'], rating_node['id'], thumbs['computerId'],
                thumbs['id'], thumbs['thumbsDown'], thumbs['thumbsUp']]

      csv_writer(file_name, header_row, data_row, teacher_rating_thumbs_lock) # Write the data to the CSV file




