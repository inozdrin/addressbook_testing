# -- author: Igor Nozdrin --
# -- Created by Igor at 3/5/2022 --
# -- coding = "utf-8" ---
import time

from selenium.webdriver.common.by import By
from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    def open_groups_page(self):
        if not (self.app.wd.current_url.endswith("/group.php") and
                len(self.wd.find_elements(By.NAME, 'new')) > 0):
            self.app.wd.find_element(By.LINK_TEXT, 'groups').click()

    def count(self):  # Count how many groups on the group page, returns
        self.open_groups_page()
        return len(self.wd.find_elements(By.NAME, 'selected[]'))

    def create_group(self, group_obj):
        self.open_groups_page()
        self.wd.find_element(By.NAME, 'new').click()
        self.fill_group_form(group_obj)
        self.wd.find_element(By.NAME, 'submit').click()
        self.group_cache = None

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

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_first_group(self):
        self.wd.find_element(By.NAME, "selected[]").click()

    def modify_group(self, group_obj):
        self.wd.find_element(By.NAME, 'edit').click()
        self.fill_group_form(group_obj)
        self.wd.find_element(By.NAME, 'update').click()
        self.group_cache = None

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element(By.NAME, "edit").click()
        self.fill_group_form(new_group_data)
        wd.find_element(By.NAME, 'update').click()
        self.open_groups_page()
        self.group_cache = None

    def delete_first_group(self):
        self.select_first_group()
        self.wd.find_element(By.NAME, "delete").click()
        self.open_groups_page()
        self.group_cache = None

    def delete_group_by_index(self, index):
        self.open_groups_page()
        self.select_group_by_index(index)
        self.wd.find_element(By.NAME, 'delete').click()
        self.open_groups_page()
        self.group_cache = None

    group_cache = None

    def get_groups_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, 'span.group'):
                txt = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=txt, id=id))
        return list(self.group_cache)
