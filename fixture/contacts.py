# -- author: Igor Nozdrin --
# -- Created by Igor at 3/2/2022 --
# -- coding = "utf-8" ---
import time

from selenium.webdriver.common.by import By
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    def add_new_contact(self, contact_obj):
        first_name_fld = self.wd.find_element(By.NAME, 'firstname')  # the first name field object
        first_name_fld.send_keys(contact_obj.first_name)
        last_name_fld = self.wd.find_element(By.NAME, 'lastname')
        last_name_fld.send_keys(contact_obj.last_name)
        home_phone_fld = self.wd.find_element(By.NAME, 'home')
        home_phone_fld.send_keys(contact_obj.home_phone)
        enter_btn = self.wd.find_element(By.NAME, 'submit')
        enter_btn.click()

    def open_contact_page(self):
        edit_page_link = self.wd.find_element(By.CSS_SELECTOR, 'li.all:nth-child(2) > a:nth-child(1)')
        edit_page_link.click()

    def create_contact(self, contact_obj):
        self.open_contact_page()

        self.add_new_contact(contact_obj)

    def get_search_count(self):
        return int(self.wd.find_element(By.ID, "search_count").text)

    def open_home_page(self):  # Home page - page with list of all contacts
        self.wd.find_element(By.CSS_SELECTOR, '#nav > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)').click()

    def count(self):  # Count how many groups on the group page, returns
        self.open_home_page()
        return len(self.wd.find_elements(By.NAME, 'selected[]')), self.get_search_count()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            list_of_rows = wd.find_elements(By.NAME, 'entry')
            for row in list_of_rows:
                firstname = row.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text
                # print("First name: " + firstname + "/n")  #  td:nth-child(3)
                lastname = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                # print("Last Name: " + lastname + "/n")
                homephone = row.find_element(By.CSS_SELECTOR, "td:nth-child(6)").text
                # print("Home phone: " + homephone + "/n")
                email = row.find_element(By.CSS_SELECTOR, "td:nth-child(5) > a:nth-child(1)").text
                # print("Email: " + email)  #  td:nth-child(5) > a:nth-child(1)
                self.contact_cache.append(Contact
                                          (first_name=firstname,
                                           last_name=lastname,
                                           home_phone=homephone,
                                           email=email))
        list_of_contacts = list(self.contact_cache)
        self.contact_cache = None
        return list_of_contacts

    def switch_to_alert_text(self):  # Returns text from the alert window
        return self.wd.switch_to.alert.text

    def switch_to_alert_accept(self):
        self.wd.switch_to.alert.accept()

    def switch_to_alert_dismiss(self):
        self.wd.switch_to.alert.dismiss()

    def delete_random_contact(self, index):
        self.open_home_page()
        rand_contact = self.wd.find_elements(By.NAME, 'selected[]')
        rand_contact[index].click()
        self.wd.find_element(By.CSS_SELECTOR, 'div.left:nth-child(8) > input:nth-child(1)').click()
        self.switch_to_alert_accept()
        self.open_home_page()
