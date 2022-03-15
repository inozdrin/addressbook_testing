# -- author: Igor Nozdrin --
# -- Created by Igor at 3/10/2022 --
# -- coding = "utf-8" ---
import time

from model.group import Group
from random import randrange


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name='test'))
    old_group_list = app.group.get_groups_list()
    index = randrange(len(old_group_list))
    app.group.delete_group_by_index(index)
    new_group_list = app.group.get_groups_list()
    assert len(old_group_list) - 1 == len(new_group_list)
    old_group_list[index:index + 1] = []
    assert old_group_list == new_group_list
