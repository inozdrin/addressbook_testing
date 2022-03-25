# -- author: Igor Nozdrin --
# -- Created by Igor at 3/24/2022 --
# -- coding = "utf-8" ---
import mysql.connector
from model.group import  Group


class DbFixture:

    def __init__(self, host, name, username, password, port=3306):
        self.host = host
        self.name = name
        self.port = port
        self.username = username
        self.password = password
        self.connection = mysql.connector.connect(host=self.host, port=self.port,
                                                  database=self.name, user=self.username,
                                                  password=self.password)

    def get_group_list(self):
        cursor = self.connection.cursor()
        group_list = []
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer  FROM group_list")
# *** cursor returns list of tuples. Each row - tuple
#           for row in cursor:
#               (id, name, header, footer) = row # in this case we assign a value to each tuple member
#               group_list.append(Group(id=id, name=name, header=header, footer=footer))
            for row in cursor.fetchall():
                group_list.append(Group(id=row[0], name=row[1], header=row[2], footer=row[3]))
        finally:
            self.connection.close()
        return group_list

    def destroy(self):
        self.connection.close()
