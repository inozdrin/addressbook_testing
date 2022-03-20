# -- author: Igor Nozdrin --
# -- Created by Igor at 3/2/2022 --
# -- coding = "utf-8" ---
import re
import time

from selenium.webdriver.common.by import By
from model.contact import Contact


def split_phones(phones):
    phone_list = list(phones.splitlines())
    final_list_phones = [""] * 4
    index = 0
    for item in phone_list:
        final_list_phones[index] = phone_list[index]
        index += 1
    return final_list_phones


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
                cells = row.find_elements(By.TAG_NAME, "td")
                id = cells[0].find_element(By.TAG_NAME, "input").get_attribute("value")
                # print(id)
                firstname = cells[2].text
                # print("First name: " + firstname + "/n")  #  td:nth-child(3)
                lastname = cells[1].text
                # print("Last Name: " + lastname + "/n")
                ph = cells[5].text
                # print("PHONES FROM CELL: " + ph + str(type(ph)))
                all_phones_list = split_phones(ph)
                # print("Home phone: " + homephone + "/n")
                email = cells[4].text
                # print("Email: " + email)  #  td:nth-child(5) > a:nth-child(1)
                self.contact_cache.append(Contact
                                          (first_name=firstname,
                                           id=id,
                                           last_name=lastname,
                                           home_phone=all_phones_list[0],
                                           mobile_phone=all_phones_list[1],
                                           work_phone=all_phones_list[2],
                                           fax_phone=all_phones_list[3],
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

    def open_contact_to_edit_by_index(self, index):
        self.open_home_page()
        row = self.wd.find_elements(By.NAME, 'entry')[index]
        cell = row.find_elements(By.TAG_NAME, 'td')[7]
        cell.find_element(By.TAG_NAME, 'a').click()

    def open_contact_to_view_by_index(self, index):
        self.open_home_page()
        row = self.wd.find_elements(By.NAME, 'entry')[index]
        cell = row.find_elements(By.TAG_NAME, 'td')[6]
        cell.find_element(By.TAG_NAME, 'a').click()

    def get_contact_info_from_view_page(self, index):
        self.open_home_page()
        self.open_contact_to_view_by_index(index)
        text = self.wd.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M:(.*)", text).group(1)
        fax = re.search("F: (.*)", text).group(1)
        return Contact(home_phone=homephone, work_phone=workphone,
                       mobile_phone=mobilephone, fax_phone=fax)

    def get_contact_info_from_edit_page(self, index):
        self.open_contact_to_edit_by_index(index)
        contact_obj = Contact()
        contact_obj.id = self.wd.find_element(By.NAME, 'id').get_attribute('value')
        contact_obj.first_name = self.wd.find_element(By.NAME, 'firstname').get_attribute('value')
        contact_obj.last_name = self.wd.find_element(By.NAME, 'lastname').get_attribute('value')
        contact_obj.home_phone = self.wd.find_element(By.NAME, 'home').get_attribute('value')
        contact_obj.mobile_phone = self.wd.find_element(By.NAME, 'mobile').get_attribute('value')
        contact_obj.work_phone = self.wd.find_element(By.NAME, 'work').get_attribute('value')
        contact_obj.fax_phone = self.wd.find_element(By.NAME, 'fax').get_attribute('value')
        return contact_obj
