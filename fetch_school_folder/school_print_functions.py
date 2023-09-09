# *****************************************************************************
# File: school_print_functions.py
# Author: Robert Boggs II
# Date: August 22, 2023
# Description: Print functions for various information about Schools
# *****************************************************************************

#----------------------------------------------------------------
#All print statments require a school_node (This holds the various data about each School)
#----------------------------------------------------------------

import textwrap
import html

def print_school(school_node: dict):
  print(f"\n               School")
  print("-"*50)
                  
  print(f"Type Name:                       {school_node['__typename']}")
  print(f"School ID:                       {school_node['id']}")
  print(f"Legacy ID:                       {school_node['legacyId']}")
  print(f"School Name:                     {school_node['name']}")
  print(f"City:                            {school_node['city']}")
  print(f"State:                           {school_node['state']}")
  print(f"Country:                         {school_node['country']}")
  print(f"Number of Ratings:               {school_node['numRatings']}")
  print(f"Average Rating:                  {school_node['avgRating']}")
  print(f"Average Rating Rounded:          {school_node['avgRatingRounded']}")

def print_school_rating_distribution(school_node: dict):
  reputationRating = float(school_node['summary']['schoolReputation'])
  foodRating = float(school_node['summary']['foodQuality'])
  locationRating = float(school_node['summary']['campusLocation'])
  clubsRating = float(school_node['summary']['clubAndEventActivities'])
  opportunitiesRating = float(school_node['summary']['careerOpportunities'])
  socialRating = float(school_node['summary']['socialActivities'])
  facilitiesRating = float(school_node['summary']['campusCondition'])
  happinessRating = float(school_node['summary']['schoolSatisfaction'])
  internetRating = float(school_node['summary']['internetSpeed'])
  safetyRating = float(school_node['summary']['schoolSafety'])

  averageRating = float(
      reputationRating+
      foodRating+
      locationRating+
      clubsRating+
      opportunitiesRating+
      socialRating+
      facilitiesRating+
      happinessRating+
      internetRating+
      safetyRating
      )/10
  
  print(f"\n       School's Rating Distribution:")
  print("-"*50)
  print(f"Average Rating:                  {averageRating}")
  print(f"Average Rating Rounded:          {round(averageRating, 2)}")
  print(f"Campus Condition:                {facilitiesRating}")
  print(f"Campus Location:                 {locationRating}")
  print(f"Career Opportunities:            {opportunitiesRating}")
  print(f"Club And Events Activities:      {clubsRating}")
  print(f"Food Quality:                    {foodRating}")
  print(f"Internet Speed:                  {internetRating}")
  print(f"School Reputation:               {reputationRating}")
  print(f"School Safety:                   {safetyRating}")
  print(f"Social Satisfaction:             {happinessRating}")
  print(f"Social Activities:               {socialRating}")


def print_school_page_info(school_node: dict):
  print(f"\n               Page Info:")
  print("-"*50)
  print(f"End Cursor:                       {school_node['ratings']['pageInfo']['endCursor']}")
  print(f"Has Next Page:                    {school_node['ratings']['pageInfo']['hasNextPage']}")

def print_school_end_cursor(school_node: dict):
  print(f"End Cursor:                       {school_node['ratings']['pageInfo']['endCursor']}")

def print_school_has_next_page(school_node: dict):
  print(f"Has Next Page:                    {school_node['ratings']['pageInfo']['hasNextPage']}")

def print_school_individual_ratings(school_node: dict):

  ratings_edges = school_node['ratings']['edges']

  for number, edge in enumerate(ratings_edges, start=1):
        
    print("-"*50)              
    print(f"\n                   Rating:")

    rating_node = edge['node']
    reputationRating = float(rating_node['reputationRating'])
    foodRating = int(rating_node["foodRating"])
    locationRating = int(rating_node['locationRating'])
    clubsRating = int(rating_node["clubsRating"])
    opportunitiesRating = int(rating_node['opportunitiesRating'])
    socialRating = int(rating_node['socialRating'])
    facilitiesRating = int(rating_node['facilitiesRating'])
    happinessRating = int(rating_node['happinessRating'])
    internetRating = int(rating_node['internetRating'])
    safetyRating = int(rating_node['safetyRating'])

    averageRating = (
      reputationRating+
      foodRating+
      locationRating+
      clubsRating+
      opportunitiesRating+
      socialRating+
      facilitiesRating+
      happinessRating+
      internetRating+
      safetyRating
      )/10

    print(f"Type Name:                        {rating_node['__typename']}")
    print(f"ID:                               {rating_node['id']}")
    print(f"Legacy ID:                        {rating_node['legacyId']}")
    print(f"Date Posted:                      {rating_node['date']}")
    print(f"Created By User:                  {rating_node['createdByUser']}")
    print(f"Average Rating:                   {averageRating}")
    print(f"Reputation Rating:                {reputationRating}")
    print(f"Food Rating:                      {foodRating}")
    print(f"Location Rating:                  {locationRating}")
    print(f"Clubs Rating:                     {clubsRating}")
    print(f"Opportunities Rating:             {opportunitiesRating}")
    print(f"Social Rating:                    {socialRating}")
    print(f"Facilities Rating:                {facilitiesRating}")
    print(f"Happiness Rating:                 {happinessRating}")
    print(f"Internet Rating:                  {internetRating}")
    print(f"Safety Rating:                    {safetyRating}")

    # #Wrap the comment text within a certain width----------------
    decoded_response_text = html.unescape(rating_node['comment'])





    wrapped_comment = textwrap.fill(decoded_response_text, width=50)
    wrapped_comment_lines = wrapped_comment.split('\n')
    print(f"Comment:                          {wrapped_comment_lines[0]}")
    for line in wrapped_comment_lines[1:]:
      print(f"                                  {line}")

    #----------------------------------------------------------------

    print(f"Flag Status:                      {rating_node['flagStatus']}")
    print(f"Thumbs Down Total:                {rating_node['thumbsDownTotal']}")
    print(f"Thumbs Up Total:                  {rating_node['thumbsUpTotal']}")

    for number, thumbs in enumerate(rating_node['userThumbs'], start=1):
      print(f"\n                   Thumb: {number}")
      print(f"Computer Id:                      {thumbs['computerId']}")
      print(f"ID:                               {thumbs['id']}")
      print(f"Thumbs Down:                      {thumbs['thumbsDown']}")
      print(f"Thumbs Up:                        {thumbs['thumbsUp']}\n")
                  
    