# -- author: Igor Nozdrin --
# -- Created by Igor at 3/24/2022 --
# -- coding = "utf-8" ---

import mysql.connector

connection = mysql.connector.connect(host="127.0.0.1", port=3306, database='addressbook', user='root', password="")

try:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM group_list")
    for row in cursor.fetchall():
        print(row)

finally:
    connection.close()
