import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    drivers = {
        "chrome": webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())),
        "firefox": webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    }
    request.cls.driver = drivers[request.param]
    yield request.cls.driver
    request.cls.driver.quit()