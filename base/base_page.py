import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    # Buttons
    CONFIRM_ACTION = ("xpath", "//span[text()='Да']")
    DISMISS_ACTION = ("xpath", "//span[text()='Нет']")

    # Push notification
    PUSH_MEET_DELETED = ("xpath", "//div[text()='Встреча удалена']")
    PUSH_MEET_CANCEL = ("xpath", "//div[text()='Встреча отменена']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    @allure.step("Click on confirm action button")
    def click_on_confirm_action_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_ACTION)).click()

    @allure.step("Click on dismiss action button")
    def click_on_dismiss_action_button(self):
        self.wait.until(EC.element_to_be_clickable(self.DISMISS_ACTION)).click()

    @allure.step("Check push meet has been delete")
    def check_push_meet_deleted(self):
        self.wait.until(EC.visibility_of_element_located(self.PUSH_MEET_DELETED))
        self.wait.until(EC.text_to_be_present_in_element(self.PUSH_MEET_DELETED, "Встреча удалена"))

    @allure.step("Check push meet has been cancel")
    def check_push_meet_cancel(self):
        self.wait.until(EC.visibility_of_element_located(self.PUSH_MEET_CANCEL))
        self.wait.until(EC.text_to_be_present_in_element(self.PUSH_MEET_CANCEL, "Встреча отменена"))

