import random
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
    SELECT_USER = ("xpath", "//p[text()='Автотест'] ")

    # Приглашение на запланированную встречу
    TOPIC_NAME = ("xpath", "//*[strong[text()='Тема встречи']]" )
    PASSWORD_MEET_FIELD = ("xpath", "//*[strong[text()='Пароль встречи']]")
    DESCRIPTION_MEET_FIELD = ("xpath", "//*[strong[text()='Описание встречи']]")
    IDENTIFICATOR_MEET_FIELD = ("xpath", "//*[strong[text()='Идентификатор встречи']]")

    # С главной страницы для проверки наличия запланированной встречи
    PLANNED_MEET_NAME_BUTTON = ("xpath", "//div[contains(@class, 'Home_content')]//div[contains(@class, 'Home_today')]//p")



    @allure.step("Add topic name")
    def add_topic(self):
        schedule_topic_field = self.wait.until(EC.element_to_be_clickable(self.SCHEDULE_TOPIC_FIELD))
        new_topic = f"Test topic{random.randint(1, 100)}"
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


    @allure.step("Add meet password")
    def add_meet_password(self):
        meet_password_field = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD))
        meet_password = f"password{random.randint(1, 100)}"
        meet_password_field.send_keys(meet_password)
        self.password = meet_password

    @allure.step("Add meet description")
    def add_meet_description(self):
        meet_description_field = self.wait.until(EC.element_to_be_clickable(self.DESCRIPTION_FIELD))
        meet_description = f"description{random.randint(1, 100)}"
        meet_description_field.send_keys(meet_description)
        self.description = meet_description

    @allure.step("Save schedule")
    def save_schedule(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Click user tab button")
    def click_user_tab_button(self):
        self.wait.until(EC.element_to_be_clickable(self.USERS_TAB)).click()

    @allure.step("Select user")
    def select_user(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_USER)).click()

    @allure.step("Check planned meet")
    def check_planned_meet(self):
        palnned_meet = self.wait.until(EC.visibility_of_all_elements_located(self.PLANNED_MEET_NAME_BUTTON))
        for element in palnned_meet:
            if element.text == self.topic:
                self.wait.until(EC.element_to_be_clickable(self.PLANNED_MEET_NAME_BUTTON))
                break
        else:
            if element == max(len(planned_meet)) :
                self.wait.until(EC.text_to_be_present_in_element(self.PLANNED_MEET_NAME_BUTTON, self.topic))


    @allure.step("Changes topic name has been saved successfuly")
    def topic_name_is_saved(self):
        self.wait.until(EC.visibility_of_element_located(self.TOPIC_NAME))
        self.wait.until(EC.text_to_be_present_in_element(self.TOPIC_NAME, self.topic))


    @allure.step("Changes password meet has been saved successfuly")
    def meet_password_is_saved(self):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_MEET_FIELD))
        self.wait.until(EC.text_to_be_present_in_element(self.PASSWORD_MEET_FIELD, self.password))


    @allure.step("Changes description has been saved successfuly")
    def meet_description_is_saved(self):
        self.wait.until(EC.visibility_of_element_located(self.DESCRIPTION_MEET_FIELD))
        self.wait.until(EC.text_to_be_present_in_element(self.DESCRIPTION_MEET_FIELD, self.description))

    @allure.step("Get meet identificator")
    def get_meet_identificator(self):
        meeting_id_text = self.wait.until(EC.visibility_of_element_located(self.IDENTIFICATOR_MEET_FIELD)).text
        meeting_id = meeting_id_text[22:]