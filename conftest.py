# -- author: Igor Nozdrin --
# -- Created by Igor at 3/5/2022 --
# -- coding = "utf-8" ---
import importlib
import time

import jsonpickle
import json
import pytest
import os
from fixture.application import Application
from fixture.db import DbFixture

fixture = None  # global var used for fixture validation
target = None


def load_config(file):
    global target

    if target is None:
        config_file = os.path.join(os.path.dirname(__file__), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


# @pytest.fixture
@pytest.fixture(scope='session')
def app(request):
    global fixture
    global target

    web_config = load_config(request.config.getoption("--target"))["web"]
    if fixture is None or not fixture.is_valid():  # Check fixture status and recreate if needed
        fixture = Application()
    fixture.session.check_tabs()
    time.sleep(5)
    fixture.session.ensure_login(username=web_config["username"], password=web_config['password'])
    time.sleep(5)
    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    dbfixture = DbFixture(host=db_config['host'],
                          name=db_config['name'],
                          port=db_config['port'],
                          username=db_config['username'],
                          password=db_config['password'])

    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")
    # parser.addoption("--browser", action="store", default="chrome")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith('json_'):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_json(file):
    with open(os.path.join(os.path.join(os.path.dirname(__file__)), "data\%s.json" % file)) as f:
        return jsonpickle.decode(f.read())


def load_from_module(module):
    return importlib.import_module("data.s%" % module).testdata


@pytest.fixture(scope='session', autouse=True)
def end_action(request):
    def finish_session():  # Function to log out and destroy session at the end of testing
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(finish_session)  # Executing at the end of the session
    return fixture
