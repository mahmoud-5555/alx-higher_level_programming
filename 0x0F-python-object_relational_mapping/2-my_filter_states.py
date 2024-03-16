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
    mydatabases = MySQLdb.Connect(host, user, password, databases)
    return mydatabases


if __name__ == "__main__":
    argumant = sys.argv
    h = "localhost"
    u = argumant[1]
    Upass = argumant[2]
    dp = argumant[3]
    search = argumant[4]

    mysatabase =\
        connect_to_mysql(host=h, user=u, password=Upass,\
                          databases=dp, port=3306)

    if mysatabase is None:
        exit(1)
    dp_pointer = mysatabase.cursor()
    dp_pointer.execute("SELECT id,name FROM states\
                       WHERE name = '{}' ORDER BY id;".format(search))
    result = dp_pointer.fetchall()
    for state in result:
        print(state)

    dp_pointer.close()
    mysatabase.close()
