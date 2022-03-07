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

    def create_group(self, group_obj):

        self.wd.find_element(By.NAME, 'new').click()
        self.fill_group_form(group_obj)
        self.wd.find_element(By.NAME, 'submit').click()

    def fill_group_form(self, group_obj):
        """"Check fields if we do not need to modify all fields"""
        self.check_mod_field("group_name", group_obj.name)
        self.check_mod_field("group_header", group_obj.header)
        self.check_mod_field('group_footer', group_obj.footer)

    def check_mod_field(self, field_name, text):
        if text is not None:
            self.wd.find_element(By.NAME, field_name).click()
            self.wd.find_element(By.NAME, field_name).clear()
            self.wd.find_element(By.NAME, field_name).send_keys(text)

    def select_first_group(self):
        self.wd.find_element(By.NAME, "selected[]").click()


    def modify_group(self, group_obj):
        self.wd.find_element(By.NAME, 'edit').click()
        self.fill_group_form(group_obj)
        self.wd.find_element(By.NAME, 'update').click()

    def delete_first_group(self):
        self.select_first_group()
        self.wd.find_element(By.NAME, "delete").click()
        self.open_groups_page()

    def get_groups_list(self):
        group_list = self.wd.find_elements(By.NAME, "selected[]")
        print(group_list)
        return group_list
