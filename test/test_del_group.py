# -- author: Igor Nozdrin --
# -- Created by Igor at 3/10/2022 --
# -- coding = "utf-8" ---
from model.group import Group


def test_delete_group(app):
    app.session.go_to_start_page()
    app.group.open_groups_page()
    print(app.group.count())
    if app.group.count() == 0:
        app.group.create_group(Group(name='test'))
    app.group.delete_first_group()
