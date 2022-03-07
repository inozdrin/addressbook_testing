# -- author: Igor Nozdrin --
# -- Created by Igor at 2/22/2022 --
# -- coding = "utf-8" ---

import time
from model.group import Group


def test_login(app):  # Log in testing
    # Call app- fixture
    app.session.check_tabs()
    #time.sleep(3)
    app.session.open_home_page()
    app.session.login()
    app.group.open_groups_page()
    #time.sleep(5)
    app.session.logout()


def test_add_group(app):
    app.session.login()
    app.group.open_groups_page()
    app.group.create_group(Group(name='new1', header='new1_header', footer='new1_footer'))
    time.sleep(3)
    app.session.logout()


def test_delete_group(app):
    app.session.login()
    app.session.open_home_page()
    app.group.open_groups_page()
    #time.sleep(3)
    app.group.delete_first_group()

    time.sleep(3)
    app.session.logout()



def test_add_contact(app):
    app.session.login()
    app.contact.create_contact(first_name='qw', last_name='er', home_phone='123')
    app.session.logout()


