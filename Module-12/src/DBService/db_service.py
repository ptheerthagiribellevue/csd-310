
"""
This module contains the DBService class which provides functionality to interact with the MySQL database.

The class has the following methods:
- connect_to_database: Attempts to connect to the WilsonFinancialDB database with the given credentials.
Returns the database connection object on success.
- close_database: Function to close database connection.
- execute_query: Function to execute SQL queries and commits.
- get_query_results: Function to execute the SQL query and return results.

"""
import mysql.connector


class DBService:

  def __init__(self):
    pass

  # Attempts to connect to the WilsonFinancialDB database with the given credentials.
  # Returns the database connection object on success.
  def connect_to_database(self):
    """
    Attempts to connect to the WilsonFinancialDB database with the given credentials.
    Returns the database connection object on success.
    """
    config = {
      "user": "root",
      "password": "mysql@01",
      "host": "127.0.0.1",
      "database": "WilsonFinancialDB"
    }
    return mysql.connector.connect(**config)

  def close_database(self, mySqlDB):
    """
    Function to close database connection.
    """
    mySqlDB.close()

  def execute_query(self, mySqlDB, query):
    """
    Function to execute SQL queries and commits.
    """
    cursor = mySqlDB.cursor()
    cursor.execute(query)
    mySqlDB.commit()

  def get_query_results(self, mySqlDB, query):
    """
    Function to execute SQL queries and returns the results as a list of tuples
    """
    cursor = mySqlDB.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    headers = [i[0] for i in cursor.description]
    return headers, results