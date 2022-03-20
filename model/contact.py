# -- author: Igor Nozdrin --
# -- Created by Igor at 3/2/2022 --
# -- coding = "utf-8" ---


class Contact:

    def __init__(self, id=None,
                 last_name=None,
                 first_name=None,
                 home_phone=None,
                 work_phone=None,
                 mobile_phone=None,
                 fax_phone=None,
                 email=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.home_phone = home_phone
        self.work_phone = work_phone
        self.mobile_phone = mobile_phone
        self.fax_phone = fax_phone
        self.email = email
