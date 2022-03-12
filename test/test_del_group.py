# -- author: Igor Nozdrin --
# -- Created by Igor at 3/10/2022 --
# -- coding = "utf-8" ---
from model.group import Group


def test_delete_group(app):
    #app.session.go_to_start_page()
    app.group.open_groups_page()
    old_group_list = app.group.get_groups_list()
    if app.group.count() == 0:
        app.group.create_group(Group(name='test'))
    app.group.delete_first_group()
    new_group_list = app.group.get_groups_list()
    assert len(old_group_list) - 1 == len(new_group_list)
    old_group_list[0:1] = []
    print(old_group_list)
    assert old_group_list == new_group_list
