# -- author: Igor Nozdrin --
# -- Created by Igor at 3/6/2022 --
# -- coding = "utf-8" ---
import time
from model.group import Group
from random import randrange


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name='test'))
    old_group_list = app.group.get_groups_list()
    index = randrange(len(old_group_list))
    group = Group(name="New name")
    group.id = old_group_list[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_group_list) == app.group.count()
    new_group_list = app.group.get_groups_list()
    old_group_list[index] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


# def test_mod_group(app):
#     app.group.open_groups_page()
#     old_group_list = app.group.get_groups_list()
#     if app.group.count() == 0:
#         app.group.create_group(Group(name='test'))
#     else:
#         app.group.select_first_group()
#         app.group.modify_group(Group(name='mod_new1____changed', header='mod_header___changed'))
#     new_group_list = app.group.get_groups_list()
#     assert len(old_group_list) == len(new_group_list)
