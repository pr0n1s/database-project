#!/usr/bin/env python

# Author: pr0n1s
# Description: Connects to MySQL database, create the database 'auth', and 
# create the tables for the database 'auth'.

import mysql.connector
from dbconfig import read_config
from mysql.connector import MySQLConnection, Error, errorcode
from database_schema import table_factory

# Description: Connects to the MySQL database.
def connect():
  # Read config.ini
  db_config = read_config()
  try:
    # Try connecting to the database
    conn = MySQLConnection(**db_config)
    # Check if we have connected
    if conn.is_connected():
      # Setup a cursor to execute SQL statements
      cursor = conn.cursor()
      # Delete the database 'auth' if it exists
      cursor.execute('DROP DATABASE auth')
      # Now create the database
      conn = create_database()
    else:
      print("Connection failed!")
  except:
    # Create database if this is the first time running the script
    conn = create_database()
  #Return MySQL connection object
  return conn

# Description: Create the database if it doesn't exist
def create_database():
  # Read config.ini
  db_config = read_config()
  host = db_config['host']
  database = db_config['database']
  user = db_config['user']
  password = db_config['password']
  try:
    # Try connecting to MySQL
    conn = mysql.connector.connect(host=host, database='', user=user, password=password)
    # Setup a cursor to execute SQL statements  
    cursor = conn.cursor()
    # Create the database 'auth'
    cursor.execute('CREATE DATABASE ' + database)
  except Error as error:
    print error
  # Return MySQL connection object
  return conn

# Arg: MySQL connection object
# Description: Create the tables in the database 'auth'
def create_tables(conn):
  # Setup a cursor to execute SQL statements
  cursor = conn.cursor()
  # Get all SQL statements to create the tables
  tables = table_factory()
  # Iterate through the tables assigning the tablename to name and the SQL
  # statement for the respective table.
  for name, sql in tables.iteritems():
    try:
      print("[*] Table: {} creating".format(name))
      # Switch to database 'auth'
      conn.database = 'auth'
      # Execute each SQL statement for each respective table
      cursor.execute(sql)
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print("[*] Table: {} already exists\n".format(name))
      else:
        print(err.msg)
    else:
      print("[*] Table: {} created\n".format(name))
