import sqlite3
from sqlite3 import Error

###############################################################################################################################################
# 1. Different version of create_connection
# In this function the database resides in RAM (temporary) not disk (permanent)
# So no database file is needed or created
# def create_connection():
#     try:
#         conn = sqlite3.connect(':memory:')
#         print(sqlite3.version)
#     except Error as e:
#         print(e)
#     finally:
#         conn.close()

# When this file is run directly run this code (won't run when this file is imported)
# if __name__ == '__main__':
#     create_connection()
###############################################################################################################################################


# 2. Functions that example.py is testing
# When you connect to an SQLite database file that does not exist, SQLite creates a new database for you.
def create_connection(db_file):
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)

	return None

def create_table(conn, statement):
    try:
        cursor = conn.cursor()
        cursor.execute(statement)
    except Error as e:
        print(e)
 
# When this file is run directly run this code (won't run when this file is imported)
if __name__ == '__main__':
	create_connection("C:\\Users\jairr\comedy_data.db")


###############################################################################################################################################
# 3. Might be necessary in the future
# def main():
# 	# Need to access somehow https://www.sqlite.org/inmemorydb.html
# 	# database = ':memory:' #?
#     database = "C:\\Users\jairr\comedy_data.db"
 
#     comedy_table = """ CREATE TABLE IF NOT EXISTS comedy (
#                                         -- id integer PRIMARY KEY,
#                                         situation text,
#                                         humor text
#                                     ); """

#     conn = create_connection(database)
#     if conn is not None:
#         create_table(conn, sql_create_projects_table)
#     else:
#         print("Error! cannot create the database connection.")

# # When this file is run directly run this code (won't run when this file is imported)
# if __name__ == '__main__':
#     main()
###############################################################################################################################################