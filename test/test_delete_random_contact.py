# -- author: Igor Nozdrin --
# -- Created by Igor at 3/15/2022 --
# -- coding = "utf-8" ---
import time
from random import randrange
from model.contact import Contact


# def test_delete_group(app):
#     if app.group.count() == 0:
#         app.group.create_group(Group(name='test'))
#     old_group_list = app.group.get_groups_list()
#     index = randrange(len(old_group_list))
#     app.group.delete_group_by_index(index)
#     new_group_list = app.group.get_groups_list()
#     assert len(old_group_list) - 1 == len(new_group_list)
#     old_group_list[index:index + 1] = []
#     assert old_group_list == new_group_list

def test_delete_random_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(last_name='Test'))
    old_contact_list = app.contact.get_contact_list()
    index = randrange(app.contact.count()[0])
    app.contact.delete_random_contact(index)
    assert len(old_contact_list) - 1 == app.contact.count()[0]


### Завтра повторить CSS_Selector - как извлечь информацию из объекта webdriver
#   Смотреть функцию app.contact.get_contact_list()

