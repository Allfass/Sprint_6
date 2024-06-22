import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions

def pytest_addoption(parser):
    parser.addoption("--headless", action="store", default="no")

@pytest.fixture(params=["firefox"])
def driver(request):
    if request.config.getoption('--headless') == 'yes':
        firefox_opts = FirefoxOptions()
        chrome_opts = ChromeOptions()
        firefox_opts.add_argument("--headless")
        chrome_opts.add_argument("--headless")
        if request.param == 'firefox':
            browser = webdriver.Firefox(options=firefox_opts)
        else:
            browser = webdriver.Chrome(options=chrome_opts)
    else:
        if request.param == 'firefox':
            browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        else:
            browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    request.cls.driver = browser
    yield request.cls.driver
    request.cls.driver.quit()