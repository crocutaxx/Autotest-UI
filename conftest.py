import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver_1(request):

    options = Options()

    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--use-fake-ui-for-media-stream")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--use-fake-device-for-media-stream")
    # options.add_argument("--use-file-for-fake-data-capture=C:/Users/User/Desktop/AutoTests/data/video1.y4m")
    options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_camera": 1
    })
    driver_1 = webdriver.Chrome(options=options)

    request.cls.driver_1 = driver_1
    yield driver_1
    driver_1.quit()

@pytest.fixture(scope="function")
def driver_2(request):

    options = Options()

    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--use-fake-ui-for-media-stream")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--use-fake-device-for-media-stream")
    # options.add_argument("--use-file-for-fake-data-capture=C:/Users/User/Desktop/AutoTests/data/video2.y4m")
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_camera": 1
    })
    driver_2 = webdriver.Chrome(options=options)

    request.cls.driver_2 = driver_2
    yield driver_2
    driver_2.quit()