# -- author: Igor Nozdrin --
# -- Created by Igor at 3/24/2022 --
# -- coding = "utf-8" ---


def test_group_lists(app,db):
    ui_group_list = app.group.get_groups_list()

    db_group_list = db.get_group_list()
    assert len(ui_group_list) == len(db_group_list)
