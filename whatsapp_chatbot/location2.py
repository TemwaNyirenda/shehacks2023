# !/usr/bin/python

import sqlite3
from geopy.distance import great_circle as GRC




def find_volunteer(latitude, longitude):
   warrior_latitude = float(latitude)
   warrior_longitude = float(longitude)

   warrior_location = (latitude, longitude)

   return find_in_database(warrior_location)

def find_in_database(warrior_location):
   row = ""

   volunteer = ""
   volunteer_num = ""

   conn = sqlite3.connect('database/volunteer_respondents.db')
   print("Opened database successfully")

   cursor = conn.execute("SELECT * FROM volunteers")
   for row in cursor:
      sh_latitude = row[4]
      sh_longitude = row[5]

      sh_location = (sh_latitude, sh_longitude)

      max_distance = row[6]

      actual_distance = find_actual_distance(warrior_location, sh_location)

      if (actual_distance <= max_distance):
         volunteer = row[1]
         volunteer_num = row[2]


   print("Operation done successfully")
   conn.close()

   return volunteer, volunteer_num

def find_actual_distance(warrior_location, sh_location):
   return GRC(warrior_location,sh_location).km


if __name__ == "__main__":
   print(find_volunteer("-25.9628634", "28.0233321"))