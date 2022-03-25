# -- author: Igor Nozdrin --
# -- Created by Igor at 2/22/2022 --
# -- coding = "utf-8" ---

import time
from model.group import Group
from sys import maxsize
import random
import string
import pytest
from data.data_test import test_data


#@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, json_groups):
    old_group_list = app.group.get_groups_list()
    group = json_groups
    app.group.create_group(group)
    new_group_list = app.group.get_groups_list()
    assert len(old_group_list) + 1 == len(new_group_list)
    old_group_list.append(group)
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


