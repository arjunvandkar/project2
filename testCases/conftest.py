import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# NOTE: keep the screenshot util import here for the hook
from utilities.screenshot_util import capture_screenshot

import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    """Command-line option for selecting browser"""
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser: chrome, firefox, or edge")


@pytest.fixture()
def setup(request):
    """Fixture to initialize the WebDriver"""
    browser = request.config.getoption("--browser").lower()

    if browser == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--disable-notifications")

        # prefer local ./drivers/msedgedriver.exe
        local_driver = os.path.join(os.getcwd(), "drivers", "msedgedriver.exe")
        if os.path.exists(local_driver):
            service_obj = EdgeService(local_driver)
        else:
            # fallback to downloader (will fail if offline)
            service_obj = EdgeService(EdgeChromiumDriverManager().install())

        driver = webdriver.Edge(service=service_obj, options=options)
        print(" Launching Edge browser...")

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference("dom.webnotifications.enabled", False)
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # <-- your path

        local_driver = os.path.join(os.getcwd(), "drivers", "geckodriver.exe")
        if os.path.exists(local_driver):
            service_obj = FirefoxService(local_driver)
        else:
            service_obj = FirefoxService(GeckoDriverManager().install())

        driver = webdriver.Firefox(service=service_obj, options=options)
        print("Launching Firefox browser...")


    else:  # default chrome
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        print("Launching Chrome browser...")

    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver  # provide driver to tests

    print(" Closing browser...")
    driver.quit()


# ---------- pytest hook to capture screenshots on failures ----------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture a screenshot automatically when a test fails (during call phase).
    It tries to obtain the WebDriver instance from the 'setup' fixture or from item.instance.driver.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        # Try common places where driver may live
        driver = item.funcargs.get("setup") or getattr(item.instance, "driver", None)
        if driver:
            test_name = rep.nodeid.replace("::", "_").replace("/", "_")
            print(f" Capturing screenshot for failed test: {test_name}")
            try:
                capture_screenshot(driver, test_name)
            except Exception as e:
                print(f" capture_screenshot raised exception: {e}")
        else:
            print("No WebDriver instance found for screenshot capture.")

########### Pytest HTML Report ###########
import os
from datetime import datetime
import pytest

def pytest_configure(config):
    config._metadata = {
        "Project Name": "Opencart",
        "Module Name": "CustRegistration",
        "Tester": "Pavan"
    }
    reports_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(reports_dir, exist_ok=True)
    report_name = datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".html"
    config.option.htmlpath = os.path.join(reports_dir, report_name)

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)




