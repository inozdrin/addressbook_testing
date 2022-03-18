# -- author: Igor Nozdrin --
# -- Created by Igor at 3/15/2022 --
# -- coding = "utf-8" ---
from model.contact import Contact


def test_add_contact(app):
    old_group_list = app.contact.get_contact_list()
    app.contact.create_contact(Contact(
        first_name='22333qw',
        last_name='sdfdsfsdfds',
        home_phone='9999999999',
        email='slkdjf;asl@lskjdf;sd'
    ))
    assert len(old_group_list) + 1 == app.contact.count()[0]  # How many contacts#
    assert len(old_group_list) + 1 == app.contact.count()[1]  # Number of contacts at the top of the page
