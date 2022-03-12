# -- author: Igor Nozdrin --
# -- Created by Igor at 2/22/2022 --
# -- coding = "utf-8" ---
#from application import Application
#from selenium.webdriver.common.by import By


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):

        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name






