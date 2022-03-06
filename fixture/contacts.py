# -- author: Igor Nozdrin --
# -- Created by Igor at 3/2/2022 --
# -- coding = "utf-8" ---
from selenium.webdriver.common.by import By
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    def add_new_contact(self, first_name, last_name, home_phone):
        first_name_fld = self.wd.find_element(By.NAME, 'firstname')  # the first name field object
        first_name_fld.send_keys(first_name)
        last_name_fld = self.wd.find_element(By.NAME, 'lastname')
        last_name_fld.send_keys(last_name)
        home_phone_fld = self.wd.find_element(By.NAME, 'home')
        home_phone_fld.send_keys(home_phone)
        enter_btn = self.wd.find_element(By.NAME, 'submit')
        enter_btn.click()

    def open_contact_page(self):
        # edit_page_link = self.wd.find_element(By.LINK_TEXT, 'edit.php')
        edit_page_link = self.wd.find_element(By.CSS_SELECTOR, 'li.all:nth-child(2) > a:nth-child(1)')
        edit_page_link.click()

    def create_contact(self, first_name, last_name, home_phone):
        new_contact = Contact(first_name, last_name, home_phone)
        self.open_contact_page()
        self.add_new_contact(new_contact.first_name, new_contact.last_name, new_contact.home_phone)
