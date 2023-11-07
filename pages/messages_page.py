import allure
from selenium.webdriver.common.keys import Keys
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class MessagesPage(BasePage):

    PAGE_URL = Links.MESSAGES_PAGE

    SEARCH_USER_FIELD = ("xpath", "//input[@class='ant-input']")
    THREE_POINT_BUTTON = ("xpath", "//*[starts-with(@class, 'ant-dropdown-trigger Search')]")
    MESSAGE_FIELD = ("xpath", "//*[@id='editor-area']")
    SEND_BUTTON =  ("xpath", "//div[@class='send-button']")
    USER_DIALOG = ("xpath", "//div[@class='Dialog_dialog__I4yGL ']")
    RESULT_OF_SEARCH = ("xpath", "//p[@class='Dialog_name__nisk7']")

    @allure.step("Search users by name")
    def enter_user_name_in_field(self):
        search_user_field = self.wait.until(EC.element_to_be_clickable(self.SEARCH_USER_FIELD))
        name_user = f"Валерий"
        search_user_field.send_keys(name_user)
        search_user_field.send_keys(Keys.ENTER)
        self.name = name_user

    @allure.step("Click on dialog")
    def click_on_user_dialog(self):
        self.wait.until(EC.element_to_be_clickable(self.USER_DIALOG)).click()
    @allure.step("Check result of search")
    def check_result_of_search(self):
        self.wait.until(EC.visibility_of_element_located(self.RESULT_OF_SEARCH))
        self.wait.until(EC.text_to_be_present_in_element(self.RESULT_OF_SEARCH, "Валерий Цой"))