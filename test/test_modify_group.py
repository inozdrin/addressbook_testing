# -- author: Igor Nozdrin --
# -- Created by Igor at 3/6/2022 --
# -- coding = "utf-8" ---
import time


def test_mod_group(app):
    app.session.login()
    app.group.open_groups_page()
    app.group.select_first_group()
    time.sleep(5)
    app.group.modify_group(name='mod_new1', header='mod_header', footer='mod_footer')
    time.sleep(3)
    app.group.open_groups_page()
    app.session.logout()
