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


def school_csv_writer(file_name: str, school_node : dict):
  # 8 Values
  header_row = ["Type Name", "School ID", "School Legacy ID", "School Name", "City", "State", 
                "Country", "Number of Ratings"]
  
  data_row = [school_node['__typename'], school_node['id'], school_node['legacyId'],
              school_node['name'], school_node['city'], school_node['state'],
              school_node['country'], school_node['numRatings']]
  
  csv_writer(file_name, header_row, data_row)


def school_rating_distribution_csv_writer(file_name: str, school_node: dict):
  #13 Values
  header_row = ["School ID", "Average Rating", "Average Rating Rounded", "Campus Condition", "Campus Location", "Career Opportunities",
                 "Club & Events Activities", "Food Quality", "Internet Speed", "School Reputation",
                 "School Safety", "Social Satisfaction", "Social Activities"]
  
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
    
  
  data_row = [school_node['id'], averageRating, round(averageRating, 2), facilitiesRating, locationRating,
              opportunitiesRating, clubsRating, foodRating, internetRating, reputationRating, safetyRating, happinessRating, socialRating]
  
  csv_writer(file_name, header_row, data_row)



def school_individual_ratings_csv_writer(file_name: str, school_node: dict):
  
  # 21 Values
  header_row = ["School ID", "Type Name", "School Rating ID", "School Rating Legacy ID", "Date Posted",
                 "Created By User", "Average Rating", "Reputation Rating",
                  "Food Rating", "Location Rating", "Clubs Rating", "Opportunities Rating",
                    "Social Rating", "Facilities Rating", "Happiness Rating", "Internet Rating",
                     "Safety Rating", "Comment", "Flag Status", "Thumbs Down Total", "Thumbs Up Total" ]
  
  ratings_edges = school_node['ratings']['edges']

  for number, edge in enumerate(ratings_edges, start=1):
    rating_node = edge['node']
    reputationRating = int(rating_node['reputationRating'])
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
    
    comment = rating_node['comment']
    if comment is not None:
      comment = html.unescape(comment)
    else: comment = ""    

    data_row =[school_node['id'], rating_node['__typename'], rating_node['id'], 
               rating_node['legacyId'], rating_node['date'], rating_node['createdByUser'],
               averageRating, reputationRating, foodRating, locationRating, clubsRating,
               opportunitiesRating, socialRating, facilitiesRating, happinessRating,
               internetRating, safetyRating, comment,
                rating_node['flagStatus'], rating_node['thumbsDownTotal'], rating_node['thumbsUpTotal']]
    
    csv_writer(file_name, header_row, data_row)




def school_rating_thumbs_csv_writer(file_name: str, school_node: dict):

  header_row = ["School ID", "Rating ID", "Computer ID", 
                "Thumb ID", "Thumbs Down", "Thumbs Up"]
  
  ratings_edges = school_node['ratings']['edges']

  for number, edge in enumerate(ratings_edges, start=1):
    rating_node = edge['node']

    for number, thumbs in enumerate(rating_node['userThumbs'], start=1):
      data_row = [school_node['id'], rating_node['id'], thumbs['computerId'], 
                  thumbs['id'], thumbs['thumbsDown'], thumbs['thumbsUp']]
      
      csv_writer(file_name, header_row, data_row)
