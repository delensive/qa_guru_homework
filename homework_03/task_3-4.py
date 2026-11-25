import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)
    yield driver
    driver.quit()


@pytest.mark.google
def test_google_web(driver):
    url = "https://www.google.com/"
    driver.get(url)
    time.sleep(5)
    assert "Google" in driver.title
    assert "google.com" in driver.current_url


@pytest.mark.github
def test_github_web(driver):
    url = "https://github.com/"
    driver.get(url)
    time.sleep(5)
    assert "GitHub" in driver.title
    assert "github.com" in driver.current_url
