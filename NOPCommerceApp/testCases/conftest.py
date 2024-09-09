import pytest
from selenium import webdriver

from utilities import ReadConfigurations
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configurations("basic info","browser")
    driver = None

    if browser.__eq__("chrome"):
        driver=webdriver.Chrome()
    elif browser.__eq__("firefox"):
        # driver = webdriver.Firefox(executable_path=r'"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"')
        driver=webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name from list chrome/firefox/edge")
    driver.maximize_window()
    app_url = ReadConfigurations.read_configurations("basic info","url")
    driver.get(app_url)
    request.cls.driver=driver
    yield
    driver.quit()