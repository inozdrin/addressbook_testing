# -- author: Igor Nozdrin --
# -- Created by Igor at 3/5/2022 --
# -- coding = "utf-8" ---
import pytest
from fixture.application import Application
from fixture.session import SessionHelper


@pytest.fixture(scope='session')
def app(request):
    fixture = Application()
    fixture.session.check_tabs()
    request.addfinalizer(fixture.destroy)
    return fixture

