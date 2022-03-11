# -- author: Igor Nozdrin --
# -- Created by Igor at 3/6/2022 --
# -- coding = "utf-8" ---
import time
from model.group import Group


def test_mod_group(app):
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.create_group(Group(name='test'))
    else:
        app.group.select_first_group()
        app.group.modify_group(Group(name='mod_new1____changed', header='mod_header___changed'))

