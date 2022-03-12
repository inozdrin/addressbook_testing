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
        if not (self.app.wd.current_url.endswith("/group.php") and
                len(self.wd.find_elements(By.NAME, 'new')) > 0):
            self.app.wd.find_element(By.LINK_TEXT, 'groups').click()

    def count(self):  # Count how many groups on the group page, returns number
        return len(self.wd.find_elements(By.NAME, 'selected[]'))

    def create_group(self, group_obj):
        self.open_groups_page()
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
        self.open_groups_page()
        # group_list = self.wd.find_elements(By.NAME, "selected[]")
        group_list = []
        for element_obj in self.app.wd.find_elements(By.CSS_SELECTOR, 'span.group'):
            text = element_obj.text
            id = element_obj.find_element(By.NAME, "selected[]").get_attribute('value')
            #print(text + " " + id)
            group_list.append(Group(name=text, id=id))
        return group_list
