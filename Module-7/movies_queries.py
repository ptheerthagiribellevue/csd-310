"""
Name: Praveen Theerthagiri
Assignment: Assignment 7.1
Date: 04/21/2023

This program connects to a MySQL database using the mysql.connector module, and performs four different types of
SELECT queries on a table in the database. The results of each query are printed to the console.

Note:
- This program assumes that the MySQL server is running and accessible.
- This program assumes that the 'movies' database with its tables exists in the database. 
"""

import mysql.connector
from mysql.connector import errorcode
import os

# Attempts to connect to the movies database with the given credentials.
# Returns the database connection object on success.
def connect_to_movies_database():
  try:
    config = {
      "user": "root",
      "password": "mysql@01",
      "host": "127.0.0.1",
      "database": "movies",
      "raise_on_warnings": True
    }
    return mysql.connector.connect(**config)
  except mysql.connector.Error as error:
    print("Error connecting to database: {}".format(error))

# Function to execute SQL queries and returns the results as a list of tuples
def execute_query(mySqldb, query):
  try:
    cursor = mySqldb.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results
  except mysql.connector.Error as error:
    print("Error executing query: {}".format(error))

# Function to print query results
def print_results(heading, columnNames, records):
    print("--- {} ---".format(heading))
    for record in records:
        print("\n".join(["{}: {}".format(columnNames[i], record[i]) for i in range(len(columnNames))]))
        print("\n")

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

# Connect to the movies database
moviesDB = connect_to_movies_database()

# Query 1: Select all records from the Studio table
studioQuery = " Select studio_id as 'Studio ID', studio_name as 'Studio Name' from studio"
studioRecords = execute_query(moviesDB, studioQuery)
column_names = ["Studio ID", "Studio Name"]
print_results("DISPLAYING Studio RECORDS", column_names, studioRecords);

# Query 2: Select all records from the genre table
genreQuery = "Select genre_id as 'Genre ID', genre_name as 'Genre Name' from genre"
genreRecords = execute_query(moviesDB, genreQuery)
column_names = ["Genre ID", "Genre Name"]
print_results("DISPLAYING Genre RECORDS", column_names, genreRecords);

# Query 3: Select records with the movie names for those movies that have a run time of less than two hours.
shortFilmQuery = "select film_name as 'Film Name', film_runtime as 'Runtime' from film where film_runtime < 120"
shortFilmRecords = execute_query(moviesDB, shortFilmQuery)
column_names = ["Film Name", "Runtime"]
print_results("DISPLAYING Short Film RECORDS", column_names, shortFilmRecords);

# Query 4: Select records with a list of film names and directors ordered by director.
directorsOrderedQuery = "select film_name as 'Film Name', film_director as 'Director' from film order by film_director asc"
directorsOrderedRecords = execute_query(moviesDB, directorsOrderedQuery)
column_names = ["Film Name", "Director"]
print_results("DISPLAYING Director RECORDS in Order", column_names, directorsOrderedRecords);

# Close the database connection
moviesDB.close()
