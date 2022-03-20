# -- author: Igor Nozdrin --
# -- Created by Igor at 3/18/2022 --
# -- coding = "utf-8" ---


def test_open_contact_to_edit(app):
    app.contact.open_contact_to_edit_by_index(4)
    # app.contact.open_home_page()


def test_open_contact_to_view(app):
    app.contact.open_contact_to_view_by_index(5)
