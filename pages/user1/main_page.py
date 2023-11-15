import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    PAGE_URL = Links.MAIN_PAGE
    # Главное окно основные кнопки
    PLANNING_MEET_BUTTON = ("xpath", "//div[text()='Запланировать']")
    NEW_MEET_BUTTON = ("xpath", "//div[text()='Новая конференция']")
    CALENDAR_BUTTON = ("xpath", "//div[text()='Календарь']")
    MESSAGES_BUTTON = ("xpath", "//div[text()='Сообщения']")
    # Главное окно доп кнопки
    CANNCELED_MEET_NAME_BUTTON = ("xpath", "//p[contains(@class, 'Home_canceled')]")
    PLANNED_MEET_NAME_BUTTON = ("xpath", "//p[contains(@class, 'Home_planned')]")
    # Взаимодействие с запланированными конференциями
    CONNECT_TO_MEET_BUTTON = ("xpath", "//span[text()='Присоединиться']")
    COPY_INVATE_BUTTON = ("xpath", "//span[text()='Скопировать приглашение']")
    EDIT_MEET_BUTTON = ("xpath", "//span[text()='Изменить']")
    CANCELL_MEET_BUTTON = ("xpath", "//span[text()='Отменить']")
    DELETE_MEET_BUTTON = ("xpath", "//span[text()='Удалить']")
    STATUS_MEET_FIELD = ("xpath", "//span[contains(@class, 'ViewSchedule_canceled')]")


    @allure.step("Click on planning meet button")
    def click_on_planning_meet_button(self):
        self.wait.until(EC.element_to_be_clickable(self.PLANNING_MEET_BUTTON)).click()

    @allure.step("Click on new meet button")
    def click_on_new_meet_button(self):
        self.wait.until(EC.element_to_be_clickable(self.NEW_MEET_BUTTON)).click()

    @allure.step("Click on calendar button")
    def click_on_calendar_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CALENDAR_BUTTON)).click()

    @allure.step("Click on messages button")
    def click_on_messages_button(self):
        self.wait.until(EC.element_to_be_clickable(self.MESSAGES_BUTTON)).click()

    @allure.step("Click on planned name meet")
    def click_on_planned_name_meet(self):
        self.wait.until(EC.visibility_of_element_located(self.PLANNED_MEET_NAME_BUTTON)).click()

    @allure.step("Click on canceled name meet")
    def click_on_canceled_name_meet(self):
        self.wait.until(EC.visibility_of_element_located(self.CANNCELED_MEET_NAME_BUTTON)).click()

    @allure.step("Click on delete meet button")
    def click_on_delete_meet_button(self):
        self.wait.until(EC.element_to_be_clickable(self.DELETE_MEET_BUTTON)).click()

    @allure.step("Click on cancell meet button")
    def click_on_cancell_meet_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CANCELL_MEET_BUTTON)).click()

    @allure.step("Click on edit meet button")
    def click_on_edit_meet_button(self):
        self.wait.until(EC.element_to_be_clickable(self.EDIT_MEET_BUTTON)).click()

    @allure.step("Click on copy invate meet button")
    def click_on_copy_in_meet_button(self):
        self.wait.until(EC.element_to_be_clickable(self.COPY_INVATE_BUTTON)).click()

    @allure.step("Click is canceled")
    def meet_is_canceled(self):
        self.wait.until(EC.visibility_of_element_located(self.STATUS_MEET_FIELD))
        self.wait.until(EC.text_to_be_present_in_element(self.STATUS_MEET_FIELD, "Отменена"))