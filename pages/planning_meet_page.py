import time

import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class PlanningMeetPage(BasePage):

    PAGE_URL = Links.PLANNING_MEET_PAGE

    # Окно планирования встречи
    SCHEDULE_TOPIC_FIELD = ("xpath", "//*[@id='schedule_topic']")
    SAVE_BUTTON = ("xpath", "//button[@type='submit']")
    CALNCELL_BUTTON = ("xpath", "//*[@id='schedule']/button[2]")
    DURATION_HOURS_FIELD = ("xpath", "//*[@id='schedule_durationHour']")
    DURATION_MINUTE_FIELD = ("xpath", "//*[@id='schedule_durationMinute']")
    DESCRIPTION_FIELD = ("xpath", "//*[@id='schedule_description']")
    WAITING_HALL_CHECKBOX = ("xpath", "//*[@id='schedule_waitingHall']")
    PASSWORD_FIELD = ("xpath", "//*[@id='schedule_password']")
    INFORMATION_TAB = ("xpath", "//div[text()='Основаня информация']")
    USERS_TAB = ("xpath", "//div[text()='Участники']")
    TEMPLATES_TAB = ("xpath", "//div[text()='Шаблоны']")
    DOCUMENTS_TAB = ("xpath", "//div[text()='Документы']")

    # Приглашение на запланированную встречу
    TOPIC_NAME = ("xpath", '//*[@id="content"]/div/div/div/p[2]' )
    PASSWORD_SCHEDULE = ("xpath", '//*[@id="content"]/div/div/div/p[7]/text()')
    DESCRIPTION_SCHEDULE = ("xpath", '//*[@id="content"]/div/div/div/p[5]/text()')


    @allure.step("Add topic name")
    def add_topic(self, new_topic):
        with allure.step(f"Add topic '{new_topic}'"):
            schedule_topic_field = self.wait.until(EC.element_to_be_clickable(self.SCHEDULE_TOPIC_FIELD))
            schedule_topic_field.send_keys(new_topic)
            self.topic = new_topic


    @allure.step("Change topic name")
    def change_topic(self, change_topic):
        with allure.step(f"Change topic on '{change_topic}'"):
            schedule_topic_field = self.wait.until(EC.element_to_be_clickable(self.SCHEDULE_TOPIC_FIELD))
            schedule_topic_field.send_keys(Keys.CTRL + "A")
            schedule_topic_field.send_keys(Keys.BACKSPACE)
            schedule_topic_field.send_keys(change_topic)
            self.topic = change_topic


    @allure.step("Save schedule")
    def save_schedule(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Changes has been saved successfuly")
    def is_saved(self):
        self.wait.until(EC.visibility_of_element_located(self.TOPIC_NAME))
        self.wait.until(EC.text_to_be_present_in_element(self.TOPIC_NAME, self.topic))