#!/usr/bin/python3
"""
this  module for connect to the data base
and print the status 
"""

import sys
import MySQLdb

def connect_to_mysql(host, user, password, databases):
	"""
	Connect to the database
	@Arge:
	host: the host that the database in
	user: the username that you wanna to assain with
	password: the password that related to the username
	database: the database that you wanna to connect with
	"""
	try:
		mydatabases = MySQLdb.Connect(host, user, password, databases)
	except:
		pass

	return mydatabases


if __name__ == "__main__":
	argumant = sys.argv
	mysatabase =  connect_to_mysql("localhost:3306", argumant[2], argumant[3], argumant[4])
	dp_pointer = mysatabase.cursor()
	dp_pointer.execute("SELECT id,name FROM states ORDER BY id;")

	for state in dp_pointer:
		print(state) 
 

