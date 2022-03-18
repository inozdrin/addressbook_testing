# -- author: Igor Nozdrin --
# -- Created by Igor at 2/22/2022 --
# -- coding = "utf-8" ---

import time
from model.group import Group
from sys import maxsize


# def test_login(app):  # Log in testing
#     # Call app- fixture
#     app.session.open_home_page()
#     app.group.open_groups_page()
#     app.session.go_to_start_page()


def test_add_group(app):
    old_group_list = app.group.get_groups_list()
    group = Group(name='NNNNNNnew1_header', footer='NNNNnew1_footer')
    app.group.create_group(group)
    new_group_list = app.group.get_groups_list()
    assert len(old_group_list) + 1 == len(new_group_list)
    old_group_list.append(group)
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


def test_add_empty_group(app):
    old_group_list = app.group.get_groups_list()
    group = Group(name='', header='', footer='')
    app.group.create_group(group)
    assert len(old_group_list) + 1 == len(app.group.get_groups_list())
    new_group_list = app.group.get_groups_list()
    old_group_list.append(group)
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


