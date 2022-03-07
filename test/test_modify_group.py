# -- author: Igor Nozdrin --
# -- Created by Igor at 3/6/2022 --
# -- coding = "utf-8" ---
import time
from model.group import Group


def test_mod_group(app):
    app.session.login()
    app.group.open_groups_page()
    app.group.select_first_group()
    time.sleep(5)
    app.group.modify_group(Group(name='mod_new1____changed', header='mod_header___changed'))
    time.sleep(3)
    app.group.open_groups_page()
    app.session.logout()
