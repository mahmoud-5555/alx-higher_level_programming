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

    for i in range(len(search)):
        if search[i] == "'":
            search = search[:i]

    mysatabase =\
        connect_to_mysql(host=h, user=u, password=Upass, databases=dp)
    dp_pointer = mysatabase.cursor()
    dp_pointer.execute("SELECT cities.name \
                        FROM cities \
                        JOIN states ON cities.state_id = states.id \
                        WHERE states.name='{}' \
                        ORDER BY cities.id;".format(search))
    result = dp_pointer.fetchall()
    p_result = ''
    for state in range(len(result)):
        if (state == 0):
            p_result += result[state][0]
        else:
            p_result = p_result + ', ' + result[state][0]

    print(p_result)

    dp_pointer.close()
    mysatabase.close()
