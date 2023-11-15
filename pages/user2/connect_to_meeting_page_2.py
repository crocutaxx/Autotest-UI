import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class ConnectToMeetingPage(BasePage):
    # Решить вопрос как прокидывать идентификатор встречи в урл для использования is_opend

    PAGE_URL = Links.CONNECT_TO_MEETING_PAGE

    IDENTIFICATOR_FIELD = ("xpath", "(//input[@id='standard-error-helper-text'])[1]")
    USER_NAME_FIELD = ("xpath", "(//input[@id='standard-error-helper-text'])[2]")
    ENTER_BUTTON = ("xpath", "//button[text()='Войти']")
    ON_MAIN_BUTTON = ("xpath", "//button[text()='На главную']")



    @allure.step("Enter meet identificator")
    def enter_meet_identificator(self):
        identificator_field = self.wait.until(EC.element_to_be_clickable(self.IDENTIFICATOR_FIELD))
        identificator_field.send_keys("666")

    @allure.step("Enter user name")
    def enter_user_name(self):
        name_field = self.wait.until(EC.element_to_be_clickable(self.USER_NAME_FIELD))
        name_field.send_keys("Test Connect")

    @allure.step("Click enter button")
    def click_enter_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ENTER_BUTTON)).click()




