import os
import configparser
import pytest

from pathlib import Path
from selenium import webdriver

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, 'config.ini')
CRED_PATH = os.path.join(ROOT_DIR, 'cred.ini')


def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="chrome", help="Type in browser type")
    parser.addoption("--url", action="store", default="http://34.218.238.101", help="url")
    parser.addoption("--hub", action="store", default="selenium-grid-aws-505804605.eu-north-1.elb.amazonaws.com", help="hub")
    parser.addoption("--environment", action="store", default="remote", help="environment")
    parser.addoption("--minio", action="store", default="http://18.219.250.237:32701", help="minio")
    parser.addoption("--region", action="store", default="eu-central-1", help="region")


@pytest.fixture(scope="function")
def driver(request):
    print("\n" + request.function.__name__ + " started")
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)

    machine = request.config.getoption("--environment")
    hub = request.config.getoption("--hub")
    if ("localhost" in machine) is True:
        hub = config.get('driver', 'hub')

    browser = webdriver.Remote(
            command_executor="http://" + hub + ":4444/wd/hub",
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


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            path = Path(__file__)
            root_dir = path.parent
            report_dir = os.path.join(root_dir, "results", "screenshots")

            name = _get_formatted_test_name(report.nodeid)
            file_name = os.path.join(report_dir, name)

            try:
                if 'driver' in item.fixturenames:
                    driver = item.funcargs['driver']
                    _capture_screenshot(driver, report_dir, name)
            except Exception as e:
                print('Exception while screen-shot creation: {}'.format(e))

            if file_name:
                html = '<a><img src="screenshots/%s.png" alt="screenshot" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></a>'%name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _get_formatted_test_name(name):
    end_index = len(name)
    start_index = name.rfind('::')
    return name[start_index+2:end_index]


def _capture_screenshot(driver, path, name):
    print("\n" + " capture screenshot " + name)

    if not os.path.isfile(path):
        try:
            os.makedirs(path)
        except OSError:
            print("Creation of the directory %s failed" % path)

    try:
        file_name = name + ".png"
        screen_name = os.path.join(path, file_name)
        driver.save_screenshot(screen_name)
    except Exception:
        print("_capture_screenshot failed")


@pytest.fixture(scope="module")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="module")
def minio(request):
    return request.config.getoption("--minio")


@pytest.fixture(scope="module")
def region(request):
    return request.config.getoption("--region")

