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
    old_group_list = app.group.get_groups_list()
    app.group.create_group(Group(name='new1', header='new1_header', footer='new1_footer'))
    new_group_list = app.group.get_groups_list()
    assert len(old_group_list) + 1 == len(new_group_list)


def test_add_contact(app):
    app.contact.create_contact(first_name='111qw', last_name='1111er', home_phone='00000123')
