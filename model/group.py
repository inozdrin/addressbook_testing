# -- author: Igor Nozdrin --
# -- Created by Igor at 2/22/2022 --
# -- coding = "utf-8" ---
# from application import Application
# from selenium.webdriver.common.by import By
from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.name, self.header, self.footer)

    def __eq__(self, other):  # Rules to compare elements(groups in this case ) in two lists
        return self.id is None or other.id is None or self.id == other.id

    def id_or_max(self):  # Check id presence and return id as int. Or set id to max for right sorting
        if self.id:
            return int(self.id)
        else:
            return maxsize
