# -- author: Igor Nozdrin --
# -- Created by Igor at 2/22/2022 --
# -- coding = "utf-8" ---
from selenium import webdriver
from selenium.webdriver.common.by import By
from model.group import Group
from model.contact import Contact
from fixture.session import SessionHelper
from fixture.contacts import ContactHelper
from fixture.groups import GroupHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome(executable_path="C:\\Chromedriver\\chromedriver.exe")
        #self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.group = GroupHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
