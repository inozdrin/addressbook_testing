# -- author: Igor Nozdrin --
# -- Created by Igor at 2/22/2022 --
# -- coding = "utf-8" ---

import time
from model.group import Group


# def test_login(app):  # Log in testing
#     # Call app- fixture
#     app.session.open_home_page()
#     app.group.open_groups_page()
#     app.session.go_to_start_page()


def test_add_group(app):
    app.group.open_groups_page()
    app.group.create_group(Group(name='new1', header='new1_header', footer='new1_footer'))


def test_delete_group(app):
    app.session.go_to_start_page()
    app.group.open_groups_page()
    app.group.delete_first_group()


def test_add_contact(app):
    app.contact.create_contact(first_name='111qw', last_name='1111er', home_phone='00000123')
