# -- author: Igor Nozdrin --
# -- Created by Igor at 3/5/2022 --
# -- coding = "utf-8" ---
import pytest
from fixture.application import Application
from fixture.session import SessionHelper

fixture = None  # global var used for fixture validation


#@pytest.fixture
@pytest.fixture(scope='session')
def app(request):
    global fixture
    if fixture is None:  # Check fixture status and recreate if needed
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.check_tabs()
    fixture.session.login()
    return fixture


@pytest.fixture(scope='session', autouse=True)
def end_action(request):
    def finish_session():  # Function to log out and destroy session at the end of testing
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(finish_session)  # Executing at the end of the session
    return fixture
