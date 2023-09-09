# *****************************************************************************
# File: teacher_print_functions.py
# Author: Robert Boggs II
# Date: August 22, 2023
# Description: Print functions for various information about teachers
# *****************************************************************************

#----------------------------------------------------------------
#All print statments require a teacher_node (This holds the various data about each Teacher)
#----------------------------------------------------------------

import textwrap
import html


def print_teacher(teacher_node: dict):
  print(f"\n               Teacher")
  print("-"*50)
                  
  print(f"Type Name:                        {teacher_node['__typename']}")
  print(f"Teacher ID:                       {teacher_node['id']}")
  print(f"Legacy ID:                        {teacher_node['legacyId']}")

  print(f"First Name:                       {teacher_node['firstName']}")
  print(f"Last Name:                        {teacher_node['lastName']}")

  print(f"Department ID:                    {teacher_node['departmentId']}")
  print(f"Department:                       {teacher_node['department']}")

  print(f"Average Difficulty:               {teacher_node['avgDifficulty']}")
  print(f"Average Rating:                   {teacher_node['avgRating']}")
  print(f"Number of Ratings:                {teacher_node['numRatings']}")
  print(f"Would Take Again Percent:         {teacher_node['wouldTakeAgainPercent']}")

  print(f"Is Professor Current User:        {teacher_node['isProfCurrentUser']}")
  print(f"Is Saved:                         {teacher_node['isSaved']}")
  print(f"Lock Status:                      {teacher_node['lockStatus']}")


def print_teacher_school(teacher_node: dict):
  print(f"\n               Teacher's School:")
  print("-"*50)
  print(f"ID:                               {teacher_node['school']['id']}")
  print(f"Legacy ID:                        {teacher_node['school']['legacyId']}")
  print(f"Name:                             {teacher_node['school']['name']}")
  print(f"Country:                          {teacher_node['school']['country']}")
  print(f"State:                            {teacher_node['school']['state']}")
  print(f"City:                             {teacher_node['school']['city']}")
  print(f"Average Rating:                   {teacher_node['school']['avgRating']}")
  print(f"Number Of Ratings:                {teacher_node['school']['numRatings']}")

def print_teacher_rating_distribution(teacher_node: dict):
  print(f"\n               Teacher's Rating Distribution:")
  print("-"*50)
  print(f"Awesome:                          {teacher_node['ratingsDistribution']['r5']}")
  print(f"Great:                            {teacher_node['ratingsDistribution']['r4']}")
  print(f"Good:                             {teacher_node['ratingsDistribution']['r3']}")
  print(f"OK:                               {teacher_node['ratingsDistribution']['r2']}")
  print(f"Awful:                            {teacher_node['ratingsDistribution']['r1']}")

def print_teacher_course_codes(teacher_node: dict):
  print(f"\n               Teacher's Course Codes:")
  print("-"*50)
  for number, course in enumerate(teacher_node['courseCodes'], start=1):
    print(f"Course {number} Name:                    {course['courseName']}")
    print(f"Course {number} Count:                   {course['courseCount']}\n")

def print_teacher_rating_tags(teacher_node: dict):
  print(f"\n               Teacher Rating Tags:")
  print("-"*50)

  for number, tag in enumerate(teacher_node['teacherRatingTags'], start = 1):
    print(f"Tag {number} ID:                         {tag['id']}")
    print(f"Legacy {number} ID:                      {tag['legacyId']}") 
    print(f"Tag  {number} Name:                      {tag['tagName']}\n")
  
def print_related_teachers(teacher_node: dict):
  print(f"\n               Teacher's Related Teachers:")
  print("-"*50)

  for number, value in enumerate(teacher_node['relatedTeachers'], start = 1):
    print(f"ID {number}:                             {value['id']}")
    print(f"Legacy ID {number}:                      {value['legacyId']}")
    print(f"First Name {number}:                     {value['firstName']}")
    print(f"Last Name {number}:                      {value['lastName']}") 
    print(f"Average Rating {number}:                 {value['avgRating']}\n")

def print_teacher_page_info(teacher_node: dict):
  print(f"\n               Page Info:")
  print("-"*50)
  print(f"End Cursor:                       {teacher_node['ratings']['pageInfo']['endCursor']}")
  print(f"Has Next Page:                    {teacher_node['ratings']['pageInfo']['hasNextPage']}")

def print_teacher_end_cursor(teacher_node: dict):
    print(f"End Cursor:                       {teacher_node['ratings']['pageInfo']['endCursor']}")

def print_teacher_has_next_page(teacher_node: dict):
    print(f"Has Next Page:                    {teacher_node['ratings']['pageInfo']['hasNextPage']}")

def print_student_ratings(teacher_node: dict):

  ratings_edges = teacher_node['ratings']['edges']

  for number, edge in enumerate(ratings_edges, start=1):

    text_book_use = rating_node['textbookUse']
    if text_book_use is not None and isinstance(text_book_use, int):
      text_book_use = "False" if text_book_use < 3 else "True"
    else:
      text_book_use = ""  

    would_take_again = rating_node['wouldTakeAgain']
    if would_take_again is not None and isinstance(would_take_again, int):
      would_take_again = "False" if would_take_again < 3 else "True"
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

    

    print("-"*50)              
    print(f"\n                   Rating:")

    rating_node = edge['node']
    print(f"Type Name:                        {rating_node['__typename']}")
    print(f"ID:                               {rating_node['id']}")
    print(f"Legacy ID:                        {rating_node['legacyId']}")
    print(f"Class:                            {rating_node['class']}")
    print(f"Date Posted:                      {rating_node['date']}")
    print(f"Admin Reviewed At:                {rating_node['adminReviewedAt']}")
    print(f"Created By User:                  {rating_node['createdByUser']}")
    print(f"Quality:                          {rating_node['clarityRating']}")
    print(f"Difficulty Rating:                {rating_node['difficultyRating']}")
    print(f"For Credit:                       {rating_node['isForCredit']}")
    print(f"Attendance:                       {attendanceMandatory}")
    print(f"Would Take Again:                 {would_take_again}")
    print(f"Grade:                            {rating_node['grade']}")
    print(f"Textbook:                         {text_book_use}")
    print(f"Online Class:                     {rating_node['isForOnlineClass']}")

    # Wrap the comment text within a certain width-----------
    decoded_response_text = html.unescape(rating_node['comment'])

    wrapped_comment = textwrap.fill(decoded_response_text, width=50)
    wrapped_comment_lines = wrapped_comment.split('\n')

    print(f"Comment:                          {wrapped_comment_lines[0]}")
    for line in wrapped_comment_lines[1:]:
      print(f"                                  {line}")
      #---------------------------------------------------------

    print(f"Helpful Rating:                   {rating_node['helpfulRating']}")

    tags = rating_node['ratingTags'].replace('--', '\n    ').replace('\n', '\n                              ')
    print(f"Rating Tags:                      {tags}")

    print(f"Flag Status:                      {rating_node['flagStatus']}")
    print(f"Teacher Note:                     {rating_node['teacherNote']}")
    print(f"Thumbs Down Total:                {rating_node['thumbsDownTotal']}")
    print(f"Thumbs Up Total:                  {rating_node['thumbsUpTotal']}")

    for number, thumbs in enumerate(rating_node['thumbs'], start=1):
      print(f"\n                   Thumb: {number}")
      print(f"Computer Id:                      {thumbs['computerId']}")
      print(f"ID:                               {thumbs['id']}")
      print(f"Thumbs Down:                      {thumbs['thumbsDown']}")
      print(f"Thumbs Up:                        {thumbs['thumbsUp']}\n")
                  
    