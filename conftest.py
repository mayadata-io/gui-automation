import os
import configparser
import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="chrome", help="Type in browser type")
    parser.addoption("--url", action="store", default="https://account.mayadata.io/login", help="url")


@pytest.fixture(scope="function")
def driver(request):
    print("\n" + request.function.__name__ + " started")

    root_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(root_dir, 'config.ini')

    config = configparser.ConfigParser()
    config.read(config_path)
    hub = config.get('driver', 'hub')

    browser = webdriver.Remote(
            command_executor="http://" + hub + "/wd/hub",
            desired_capabilities={
                "browserName": request.config.getoption("--driver")
            })

    browser.implicitly_wait(30)
    browser.maximize_window()

    def quite():
        browser.quit()
        print(request.function.__name__ + " completed")

    request.addfinalizer(quite)

    return browser


@pytest.fixture(scope="module")
def url(request):
    return request.config.getoption("--url")