from database_helpers import *

print("start")

# conn = sqlite3.connect('comedy_data.db') #this version doesn't handle error
path_db = "C:\\Users\jairr\comedy_data.db"
comedy_table = """ CREATE TABLE IF NOT EXISTS comedy (
										-- id integer PRIMARY KEY, #useful later
										situation text,
										humor text
									); """

conn = create_connection(path_db) 

if conn is not None:
	print("doing")

	cursor = conn.cursor()
    # cursor.execute(statement) #this version doesn't handle error
	create_table(conn, comedy_table)
	cursor.execute("INSERT INTO comedy VALUES ('bar','dark')")
	cursor.execute("INSERT INTO comedy VALUES ('chicken','surreal')")
	conn.commit()

	print("print rows")
	for row in cursor.fetchall():
		print(row)

	# cursor.close()

print("done")



###############################################################################################################################################
# from database_helpers import *

# conn = sqlite3.connect('comedy_data.db') 
# comedy_table = """ CREATE TABLE IF NOT EXISTS comedy (
# 										-- id integer PRIMARY KEY, #useful later
# 										situation text,
# 										humor text
# 									); """
# cursor = conn.cursor()
# cursor.execute(comedy_table)
# cursor.execute("INSERT INTO comedy VALUES ('bar','dark')")
# cursor.execute("INSERT INTO comedy VALUES ('chicken','surreal')")
# conn.commit()

# for row in cursor.fetchall():
# 	print(row)
###############################################################################################################################################