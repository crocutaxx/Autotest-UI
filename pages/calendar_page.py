import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class CalendarPage(BasePage):

    PAGE_URL = Links.CALENDAR_PAGE