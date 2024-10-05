"""Module providing a function printing python version."""

print("hello")

import mysql.connector

cnx = mysql.connector.connect(user="scott", password="S@LtPepp3r@",
                              host="127.0.0.1",
                              database="employees")
cnx.close()
