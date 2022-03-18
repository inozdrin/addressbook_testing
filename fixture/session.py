# -- author: Igor Nozdrin --
# -- Created by Igor at 3/2/2022 --
# -- coding = "utf-8" ---
from selenium.webdriver.common.by import By

""" 
The major fixture app contains link to initialized webdriver
"""


class SessionHelper:
    def __init__(self, app):  # app - major fixture object
        self.app = app

    def open_home_page(self):
        homepage_url = 'http://localhost/addressbook/'
        self.app.wd.get(homepage_url)

    def go_to_start_page(self):
        self.app.wd.find_element(By.CSS_SELECTOR, "#nav > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)").click()

    def check_tabs(self):  # Checking if Chrome Settings  Tab opens when browser starts

        if len(self.app.wd.window_handles) > 1:
            current_window = self.app.wd.window_handles[1]
            chrome_sett_tab = self.app.wd.window_handles[0]
            self.app.wd.switch_to.window(chrome_sett_tab)
            self.app.wd.close()
            self.app.wd.switch_to.window(current_window)
            self.app.wd.maximize_window()
        else:
            pass

    def login(self, username, password):
        self.open_home_page()
        username_fld = self.app.wd.find_element(By.NAME, 'user')

        username_fld.click()
        username_fld.clear()
        username_fld.send_keys(username)
        password_fld = self.app.wd.find_element(By.NAME, 'pass')
        password_fld.click()
        password_fld.clear()
        password_fld.send_keys(password)
        login_btn = self.app.wd.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        login_btn.click()

    def logout(self):
        # self.app.wd.find_element(By.CSS_SELECTOR, '.header > a:nth-child(3)').click()

        self.app.wd.find_element(By.LINK_TEXT, "Logout").click()
        # .header > a: nth - child(3)
        # .header > a: nth - child(3)
        # self.app.wd.quit()

    def logged_in_as(self, username):  # Check - logged in the right user
        u_name = self.get_logged_user()
        return u_name == '%s' % username

    def get_logged_user(self):
        return self.app.wd.find_element(By.CSS_SELECTOR, '.header > b:nth-child(2)').text[1:-1]

    def ensure_login(self, username, password):
        # Checking log in under right username and re-login if needed
        if self.is_logged_in():
            if self.logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):  # Check the presence of Logout element. Returns true or False
        return len(self.app.wd.find_elements(By.LINK_TEXT, "Logout")) > 0

    def destroy_session(self):
        self.app.wd.quit()
