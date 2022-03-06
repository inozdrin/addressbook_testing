# -- author: Igor Nozdrin --
# -- Created by Igor at 3/5/2022 --
# -- coding = "utf-8" ---
from selenium.webdriver.common.by import By
from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    def open_groups_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, 'groups').click()

    def create_group(self, name, header, footer):
        new_group = Group(name, header, footer)
        self.wd.find_element(By.NAME, 'new').click()
        self.wd.find_element(By.NAME, 'group_name').click()
        self.wd.find_element(By.NAME, 'group_name').clear()
        self.wd.find_element(By.NAME, 'group_name').send_keys(new_group.name)
        self.wd.find_element(By.NAME, 'group_header').click()
        self.wd.find_element(By.NAME, 'group_header').clear()
        self.wd.find_element(By.NAME, 'group_header').send_keys(new_group.header)
        self.wd.find_element(By.NAME, 'group_footer').click()
        self.wd.find_element(By.NAME, 'group_footer').clear()
        self.wd.find_element(By.NAME, 'group_footer').send_keys(new_group.footer)
        self.wd.find_element(By.NAME, 'submit').click()

    def delete_first_group(self):
        self.wd.find_element(By.NAME, "selected[]").click()
        self.wd.find_element(By.NAME, "delete").click()

    def get_groups_list(self):
        group_list = self.wd.find_elements(By.NAME, "selected[]")
        print(group_list)
        return group_list
