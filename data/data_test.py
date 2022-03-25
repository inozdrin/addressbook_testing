# -- author: Igor Nozdrin --
# -- Created by Igor at 3/23/2022 --
# -- coding = "utf-8" ---

from model.group import Group
import random
import string



def rand_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits  + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Group(name="", header="", footer="")] + \
            [Group(name=rand_string("name", 10), header=rand_string("header", 20),
                   footer=rand_string("footer", 20))
             for i in range(10)
             ]
