import time

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
    LIST_TODAY_MEETS = ("xpath", "//div[contains(@class, 'Home_content')]")
    CANCELED_MEET_NAME_BUTTON = ("xpath", "//p[contains(@class, 'Home_canceled')]")
    PLANNED_MEET_NAME_BUTTON = ("xpath", "//p[contains(@class, 'Home_planned') and contains(text(), 'Test ')]")
    WAITING_ROOM_MEET_NAME_BUTTON = ("xpath", "//p[contains(@class, 'Home_planned') and contains(text(), 'Waiting')]")
    BLOСKED_ROOM_MEET_NAME_BUTTON = ("xpath", "//p[text()='Blocked meet']")
    CREATE_ROOM_MEET_NAME_BUTTON = ("xpath", "//p[text()='Create room']")
    # Взаимодействие с запланированными конференциями
    VIEWING_WINDOW_WIDGET = ("xpath", "//div[@class = 'ant-modal-content']")
    CONNECT_TO_MEET_BUTTON = ("xpath", "//span[text()='Присоединиться']")
    COPY_INVITE_BUTTON = ("xpath", "//span[text()='Скопировать приглашение']")
    EDIT_MEET_BUTTON = ("xpath", "//span[text()='Изменить']")
    CANCEL_MEET_BUTTON = ("xpath", "//span[text()='Отменить']")
    DELETE_MEET_BUTTON = ("xpath", "//span[text()='Удалить']")
    STATUS_MEET_FIELD = ("xpath", "//span[contains(@class, 'ViewSchedule_canceled')]")
    STATUS_BLOCKED_FIELD = ("xpath", "//p[contains(@class, 'ViewSchedule_form')][last()]/span[2]")
    MEET_FOR_DELETE = ("xpath", "//p[text()='Delete room']")
    @allure.step("Click on planning meet button")
    def click_on_planning_meet_button(self):
        self.wait.until(EC.element_to_be_clickable(self.PLANNING_MEET_BUTTON)).click()

    @allure.step("Click on new meet button")
    def click_on_new_meet_button(self):
        self.wait.until(EC.element_to_be_clickable(self.NEW_MEET_BUTTON)).click()

    @allure.step("Click on connect to meet button")
    def click_on_connect_to_meet_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CONNECT_TO_MEET_BUTTON)).click()

    @allure.step("Click on calendar button")
    def click_on_calendar_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CALENDAR_BUTTON)).click()

    @allure.step("Click on messages button")
    def click_on_messages_button(self):
        self.wait.until(EC.element_to_be_clickable(self.MESSAGES_BUTTON)).click()

    @allure.step("Click on planned name meet")
    def click_on_planned_name_meet(self):
        self.wait.until(EC.visibility_of_element_located(self.PLANNED_MEET_NAME_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.VIEWING_WINDOW_WIDGET))
    @allure.step("Click on meet name button")
    def click_on_waiting_meet_button(self):
        self.wait.until(EC.element_to_be_clickable(self.WAITING_ROOM_MEET_NAME_BUTTON)).click()

    @allure.step("Click on meet name button")
    def click_on_meet_for_block_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BLOСKED_ROOM_MEET_NAME_BUTTON)).click()

    @allure.step("Click on meet name button")
    def click_on_meet_for_create_room_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_ROOM_MEET_NAME_BUTTON)).click()

    @allure.step("Click on meet name button")
    def click_on_meet_for_delete_button(self):
        self.wait.until(EC.element_to_be_clickable(self.MEET_FOR_DELETE)).click()

    @allure.step("Click on canceled name meet")
    def click_on_canceled_name_meet(self):
        self.wait.until(EC.visibility_of_element_located(self.CANCELED_MEET_NAME_BUTTON)).click()

    @allure.step("Click on delete meet button")
    def click_on_delete_meet_button(self):
        self.wait.until(EC.element_to_be_clickable(self.DELETE_MEET_BUTTON)).click()

    @allure.step("Click on cancell meet button")
    def click_on_cancell_meet_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CANCEL_MEET_BUTTON)).click()

    @allure.step("Click on edit meet button")
    def click_on_edit_meet_button(self):
        self.wait.until(EC.element_to_be_clickable(self.EDIT_MEET_BUTTON)).click()

    @allure.step("Click on copy invite meet button")
    def click_on_copy_in_meet_button(self):
        self.wait.until(EC.element_to_be_clickable(self.COPY_INVITE_BUTTON)).click()

    @allure.step("Click is canceled")
    def meet_is_canceled(self):
        self.wait.until(EC.visibility_of_element_located(self.STATUS_MEET_FIELD))
        self.wait.until(EC.text_to_be_present_in_element(self.STATUS_MEET_FIELD, "Отменена"))

    @allure.step("Click is canceled")
    def meet_is_blocked(self):
        self.wait.until(EC.visibility_of_element_located(self.STATUS_BLOCKED_FIELD))
        self.wait.until(EC.text_to_be_present_in_element(self.STATUS_BLOCKED_FIELD, "blocked"))

    @allure.step("Meet is deleted")
    def meet_is_deleted(self):
        self.wait.until(EC.invisibility_of_element_located(self.MEET_FOR_DELETE))


    # def save_cookie(self):
    #     time.sleep(5)
    #     cookies = self.driver.execute_cdp_cmd("Network.getAllCookies", {})
    #     print(cookies)

    # @allure.step("clear today meets")
    # def clear_today_meets(self):
    #     today_list = self.wait.until(EC.visibility_of_all_elements_located(self.LIST_TODAY_MEETS))
    #     if len(today_list) != 0:
    #         planned_meet = self.wait.until(EC.visibility_of_all_elements_located(self.PLANNED_MEET_NAME_BUTTON))
    #         while len(planned_meet) != 0 :
    #             self.wait.until(EC.visibility_of_element_located(self.PLANNED_MEET_NAME_BUTTON))
    #             self.wait.until(EC.element_to_be_clickable(self.PLANNED_MEET_NAME_BUTTON)).click()
    #             self.wait.until(EC.element_to_be_clickable(self.DELETE_MEET_BUTTON)).click()
    #
    #         bloked_meet = self.wait.until(EC.visibility_of_all_elements_located(self.BLOСKED_ROOM_MEET_NAME_BUTTON))
    #         while len(bloked_meet) != 0:
    #             self.wait.until(EC.visibility_of_element_located(self.BLOСKED_ROOM_MEET_NAME_BUTTON))
    #             self.wait.until(EC.element_to_be_clickable(self.BLOСKED_ROOM_MEET_NAME_BUTTON)).click()
    #             self.wait.until(EC.element_to_be_clickable(self.DELETE_MEET_BUTTON)).click()
    #
    #         canceled_meet = self.wait.until(EC.visibility_of_all_elements_located(self.CANNCELED_MEET_NAME_BUTTON))
    #         while len(create_meet) != 0:
    #             self.wait.until(EC.visibility_of_element_located(self.CANNCELED_MEET_NAME_BUTTON))
    #             self.wait.until(EC.element_to_be_clickable(self.CANNCELED_MEET_NAME_BUTTON)).click()
    #             self.wait.until(EC.element_to_be_clickable(self.DELETE_MEET_BUTTON)).click()

