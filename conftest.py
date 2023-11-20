import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver_1(request):
    try:
        options = Options()

        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--use-fake-ui-for-media-stream")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

        request.cls.driver = driver
        yield driver
    finally:
        driver.quit()

@pytest.fixture(scope="function")
def driver_2(request):
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--use-fake-ui-for-media-stream")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

        request.cls.driver = driver
        yield driver
    finally:
        driver.quit()