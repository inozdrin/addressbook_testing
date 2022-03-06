# -- author: Igor Nozdrin --
# -- Created by Igor at 3/2/2022 --
# -- coding = "utf-8" ---
from selenium.webdriver.common.by import By

# from fixture.application import Application
""" 
The major fixture app contains link to initialized webdriver
"""


class SessionHelper:
    def __init__(self, app):  # app - major fixture object
        self.app = app

    def open_home_page(self):
        homepage_url = 'http://localhost/addressbook/'
        self.app.wd.get(homepage_url)

    def check_tabs(self):  # Checking if Chrome Settings  Tab opens when browser starts

        if len(self.app.wd.window_handles) > 1:
            current_window = self.app.wd.window_handles[1]
            chrome_sett_tab = self.app.wd.window_handles[0]
            self.app.wd.switch_to.window(chrome_sett_tab)
            self.app.wd.close()
            self.app.wd.switch_to.window(current_window)
        else:
            pass

    def login(self):
        self.open_home_page()
        username = self.app.wd.find_element(By.NAME, 'user')

        username.click()
        username.clear()
        username.send_keys('admin')
        password = self.app.wd.find_element(By.NAME, 'pass')
        password.click()
        password.clear()
        password.send_keys('secret')
        login_btn = self.app.wd.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        login_btn.click()

    def logout(self):
        self.app.wd.find_element(By.CSS_SELECTOR, '.header > a:nth-child(3)').click()
        # self.app.wd.quit()

    def destroy_session(self):
        self.app.wd.quit()
