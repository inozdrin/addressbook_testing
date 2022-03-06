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
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.group = GroupHelper(self)


        # if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(By.NAME, "new")) > 0):
        #   wd.find_element(By.LINK_TEXT, "groups").click()





    def destroy(self):
        self.wd.quit()
