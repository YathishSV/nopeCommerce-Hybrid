from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\tutorial\\driver executables\\chromedriver.exe")
        print("================Starting Chrome Browser==================")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\tutorial\\driver executables\\geckodriver.exe")
        print("================Starting Firefox Browser==================")
    else:
        driver = webdriver.Chrome(executable_path="C:\\tutorial\\driver executables\\chromedriver.exe")
        print("================Starting Chrome Browser==================")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata["Project Name"] = 'nop eCommerce'
    config._metadata["Module Name"] = 'Customers'
    config._metadata["Tester"] = "Yathish"


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
