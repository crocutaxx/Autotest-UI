import allure
import random
from selenium.webdriver.common.keys import Keys
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class MessagesPage(BasePage):

    PAGE_URL = Links.MESSAGES_PAGE

    SEARCH_USER_FIELD = ("xpath", "//input[@class='ant-input']")
    THREE_POINT_BUTTON = ("xpath", "//*[starts-with(@class, 'ant-dropdown-trigger Search')]")
    MESSAGE_FIELD = ("xpath", "//*[@id='editor-area']")
    SEND_MESSAGE_BUTTON =  ("xpath", "//div[@class='send-button']")
    USER_DIALOG = ("xpath", "//div[contains(@class, 'Dialog_dialog')][1]")
    RESULT_OF_SEARCH = ("xpath", "//p[contains(@class, 'Dialog_name')][1]")
    USER_CHAT = ("xpath", "//div[@class='user-name']")
    COUNTER_UNREAD_MESSAGES = ("xpath", "//span[contains(@class, 'Dialog_unreadMessage__')]")
    LAST_MESSAGE = ("xpath", "(//span[@class='message-text'])[last()]")

    @allure.step("Search users by name")
    def enter_user_name_in_field(self):
        search_user_field = self.wait.until(EC.element_to_be_clickable(self.SEARCH_USER_FIELD))
        name_user = f"Автотест"
        search_user_field.send_keys(name_user)
        search_user_field.send_keys(Keys.ENTER)
        self.name = name_user + " Второй"

    @allure.step("Click on dialog")
    def click_on_user_dialog(self):
        self.wait.until(EC.element_to_be_clickable(self.USER_DIALOG)).click()
    @allure.step("Check result of search")
    def check_result_of_search(self):
        self.wait.until(EC.visibility_of_element_located(self.RESULT_OF_SEARCH))
        self.wait.until(EC.text_to_be_present_in_element(self.RESULT_OF_SEARCH, self.name))
    @allure.step("Enter message")
    def enter_message(self):
        message_field = self.wait.until(EC.element_to_be_clickable(self.MESSAGE_FIELD))
        self.message = f"message{random.randint(1, 100)}"
        message_field.send_keys(self.message)
    @allure.step("Send message")
    def send_message(self):
        self.wait.until(EC.element_to_be_clickable(self.SEND_MESSAGE_BUTTON)).click()

    @allure.step("User chat is opend")
    def user_chat_is_opdend(self):
        self.wait.until(EC.visibility_of_element_located(self.USER_CHAT))
        self.wait.until(EC.text_to_be_present_in_element(self.USER_CHAT, self.name))

    @allure.step("Check unread message")
    def check_unread_message(self):
        self.wait.until(EC.visibility_of_element_located(self.COUNTER_UNREAD_MESSAGES))
        self.wait.until(EC.text_to_be_present_in_element(self.COUNTER_UNREAD_MESSAGES, "1"))
    @allure.step("Check last message")
    def check_last_message(self):
        self.wait.until(EC.visibility_of_element_located(self.LAST_MESSAGE))
        self.wait.until(EC.text_to_be_present_in_element(self.LAST_MESSAGE, self.message))
