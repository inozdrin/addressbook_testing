# -- author: Igor Nozdrin --
# -- Created by Igor at 3/18/2022 --
# -- coding = "utf-8" ---
import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]  # got Contact object
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)  # got Contact object
    assert contact_from_home_page.home_phone == clear(contact_from_edit_page.home_phone)
    assert contact_from_home_page.work_phone == clear(contact_from_edit_page.work_phone)
    assert contact_from_home_page.mobile_phone == clear(contact_from_edit_page.mobile_phone)
    assert contact_from_home_page.fax_phone == clear(contact_from_edit_page.fax_phone)


def test_phones_on_contact_view_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]  # got Contact object
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)  # got Contact object
    assert contact_from_home_page.home_phone == clear(contact_from_view_page.home_phone)
    assert contact_from_home_page.work_phone == clear(contact_from_view_page.work_phone)
    assert contact_from_home_page.mobile_phone == clear(contact_from_view_page.mobile_phone)
    #assert contact_from_home_page.fax_phone == contact_from_view_page.fax_phone


def clear(string_to_clear):
    return re.sub("[]()! *-]", "", string_to_clear)
