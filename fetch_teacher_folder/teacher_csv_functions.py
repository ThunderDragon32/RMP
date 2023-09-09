import os
import csv
import html

def csv_writer(file_name, header_row, data_row):
  file_exists = os.path.isfile(file_name) and os.path.getsize(file_name) > 0

  with open(file_name, mode='a', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    if not file_exists:
      csv_writer.writerow(header_row)

    csv_writer.writerow(data_row)


def teacher_csv_writer(file_name: str, teacher_node: dict):
    
  header_row = ["Type Name", "Teacher ID", "Teacher Legacy ID", "First Name", 
                  "Last Name", "Department ID", "Department", "Average Difficulty", 
                  "Average Rating", "Number of Ratings", "Would Take Again Percent", 
                  "Is Professor Current User", "Is Saved", "Lock Status", "School ID",
                    "Awesome", "Great", "Good", "OK", "Awful"]

  # 20 Values


  data_row = [teacher_node['__typename'], teacher_node['id'],teacher_node['legacyId'], 
                teacher_node['firstName'],teacher_node['lastName'], teacher_node['departmentId'],
                  teacher_node['department'], teacher_node['avgDifficulty'], teacher_node['avgRating'],  
                  teacher_node['numRatings'], teacher_node['wouldTakeAgainPercent'], teacher_node['isProfCurrentUser'],
                     teacher_node['isSaved'], teacher_node['lockStatus'], teacher_node['school']['id'], 
                     teacher_node['ratingsDistribution']['r5'], teacher_node['ratingsDistribution']['r4'], teacher_node['ratingsDistribution']['r3'],
                        teacher_node['ratingsDistribution']['r2'], teacher_node['ratingsDistribution']['r1']]
    
  csv_writer(file_name, header_row, data_row)




def teacher_course_codes_csv_writer(file_name : str, teacher_node: dict):
  # 3 Values
  header_row = ["Teacher ID", "Course Name", "Course Count"]

  for number, course in enumerate(teacher_node['courseCodes'], start=1):
    data_row = [teacher_node['id'], course['courseName'], course['courseCount']]
      
    csv_writer(file_name, header_row, data_row)


     
def teacher_rating_tags_csv_writer(file_name : str, teacher_node: dict):
  # 4 Values
  header_row = ["Teacher ID", "Tag ID", "Tag Legacy ID", "Tag Name"]

  for number, tag in enumerate(teacher_node['teacherRatingTags'], start = 1):

    data_row = [teacher_node['id'], tag['id'], tag['legacyId'], tag['tagName']]
    csv_writer(file_name, header_row, data_row)



def teacher_related_teachers_csv_writer(file_name : str, teacher_node: dict):
  # 6 Values
  header_row = ["Teacher ID", "Related Teacher ID", "Related Teacher ID", "First Name", "Last Name", "Average Rating"]


  for number, value in enumerate(teacher_node['relatedTeachers'], start = 1):
    
    data_row = [teacher_node['id'], value['id'], value['legacyId'], value['firstName'], value['lastName'], value['avgRating']]
    
    csv_writer(file_name, header_row, data_row)



def student_ratings_csv_writer(file_name: str, teacher_node: dict):

  # 21 Values
  header_row = ["Teacher ID", "Type Name", "Rating ID", "Rating Legacy ID", "Class", "Date Posted", "Admin Reviewed At",
                 "Created By User", "Quality", "Difficulty", "For Credit", "Attendance", "Would Take Again",
                 "Grade", "Textbook", "Online Class", "Comment", "Flag Status", "Teacher Note", "Thumbs Down Total", "Thumbs Up Total"]

  ratings_edges = teacher_node['ratings']['edges']

  for number, edge in enumerate(ratings_edges, start=1):
    rating_node = edge['node']

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


    data_row = [teacher_node['id'], rating_node['__typename'], rating_node['id'], 
                rating_node['legacyId'], rating_node['class'], rating_node['date'], 
                rating_node['adminReviewedAt'], rating_node['createdByUser'], 
                rating_node['clarityRating'], rating_node['difficultyRating'],
                rating_node['isForCredit'], attendanceMandatory,
                would_take_again, rating_node['grade'], text_book_use,
                rating_node['isForOnlineClass'], html.unescape(rating_node['comment']),
                rating_node['flagStatus'], rating_node['teacherNote'], rating_node['thumbsDownTotal'],
                rating_node['thumbsUpTotal']] 

    
    csv_writer(file_name, header_row, data_row)


def teacher_rating_thumbs_csv_writer(file_name : str, teacher_node : dict):

  # 6 Values
  header_row = ["Teacher ID", "Rating ID", "Computer ID", "Thumb ID", "Thumb Down", "Thumb Up"]

  ratings_edges = teacher_node['ratings']['edges']
  for number, edge in enumerate(ratings_edges, start=1):
    rating_node = edge['node']


    for number, thumbs in enumerate(rating_node['thumbs'], start=1):

      data_row = [teacher_node['id'], rating_node['id'], thumbs['computerId'],
                thumbs['id'], thumbs['thumbsDown'], thumbs['thumbsUp']]

      csv_writer(file_name, header_row, data_row)




