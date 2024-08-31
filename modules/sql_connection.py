import datetime
import mysql.connector

__cnx = None

db_config = {
    'host': 'sql12.freesqldatabase.com',
    'user': 'sql12728780',
    'password': 'UIJimdww2D',
    'database': 'sql12728780'
}

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:
    __cnx = mysql.connector.connect(**db_config)

  return __cnx




