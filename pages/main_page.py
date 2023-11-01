import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    PAGE_URL = Links.MAIN_PAGE

    PLANNING_MEET_BUTTON = ("xpath", "//div[text()='Запланировать']")
    NEW_MEET_BUTTON = ("xpath", "//div[text()='Новая конференция']")
    CALENDAR_BUTTON = ("xpath", "//div[text()='Календарь']")
    MESSAGES_BUTTON = ("xpath", "//div[text()='Сообщения']")

    @allure.step("Click on planning meet button")
    def click_on_planning_meet_button(self):
        self.wait.until(EC.element_to_be_clickable(self.PLANNING_MEET_BUTTON)).click()

    @allure.step("Click on planning meet button")
    def click_on_new_meet_button(self):
        self.wait.until(EC.element_to_be_clickable(self.NEW_MEET_BUTTON)).click()

    @allure.step("Click on planning meet button")
    def click_on_calendar_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CALENDAR_BUTTON)).click()

    @allure.step("Click on planning meet button")
    def click_on_messages_button(self):
        self.wait.until(EC.element_to_be_clickable(self.MESSAGES_BUTTON)).click()