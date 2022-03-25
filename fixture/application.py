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
    def __init__(self, browser='chrome'):
        # self.wd = webdriver.browser
        if browser == 'firefox':
            self.wd = webdriver.Firefox(executable_path="C:\\SeleniumWebdrivers\\geckodriver.exe")
        elif browser == 'edge':
            self.wd == webdriver.Edge(executable_path="C:\\SeleniumWebdrivers\\msedgedriver.exe")
            # self.wd == webdriver.Edge()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome(executable_path="C:\\Chromedriver\\chromedriver.exe")
        else:
            raise ValueError('Could not recognize %s!' % browser)
        #self.wd = webdriver.Firefox()
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

    def swithch(self):
        alert_obj = self.wd.switch_to.alert
        alert_obj.accept()
