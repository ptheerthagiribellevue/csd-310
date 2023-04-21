"""
Name: Praveen Theerthagiri
Assignment: Assignment 8.1
Date: 04/21/2023

This program connects to a MySQL database using the mysql.connector module, and performs CRUD operations on the movies database.
SELECT queries on a table in the database. The results of each CRUD operation is printed to the console.

Note:
- This program assumes that the MySQL server is running and accessible.
- This program assumes that the 'movies' database with its tables exists in the database. 
"""

import mysql.connector
from mysql.connector import errorcode
import os

# Attempts to connect to the movies database with the given credentials.
# Returns the database connection object on success.
def get_movies_database_cursor():
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

# Displays the movies information
def show_films(cursor, title):
   filmsQuery = '''Select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' 
                     from film 
                        INNER JOIN Genre on film.Genre_id = Genre.Genre_id
                        INNER JOIN Studio on film.Studio_id = Studio.Studio_id'''
   cursor.execute(filmsQuery)
   films = cursor.fetchall()

   print("\n --- {} ---".format(title))

   for film in films:
      print("Film Name: {}\nDirector: {}\nGenre Name: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

#Inserts a new movie
def insert_film(cursor):
   insertFilmQuery = '''insert into film (film_id, film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) 
                        values (4, 'The Invisible Man', 2020, 124, 'Leigh Whannell', 3, 1)'''
   cursor.execute(insertFilmQuery)

#Updates the genre of film - Alien
def update_Alien_film_to_horror(cursor):
   updateFilmQuery = "Update film set genre_id = 1 where film_id = 2"
   cursor.execute(updateFilmQuery)

#Deletes a film - Gladiator
def delete_Gladiator_film(cursor):
   deleteFilmQuery = "Delete from film where film_id = 1"
   cursor.execute(deleteFilmQuery)

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

# movies cursor connected DB
moviesDB = get_movies_database_cursor()
moviesDBCursor = moviesDB.cursor()

#displaying films
show_films(moviesDBCursor, "DISPLAYING FILMS")

#insert new film
insert_film(moviesDBCursor)

#displaying films
show_films(moviesDBCursor, "DISPLAYING FILMS AFTER INSERT")

#update Alien film to horror
update_Alien_film_to_horror(moviesDBCursor)

#displaying films
show_films(moviesDBCursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

#delete gladiator film
delete_Gladiator_film(moviesDBCursor)

#displaying films
show_films(moviesDBCursor, "DISPLAYING FILMS AFTER DELETE")

moviesDBCursor.close()
moviesDB.close()

