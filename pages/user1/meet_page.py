import allure
import time
import keyboard
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class MeetPage(BasePage):
    # Решить вопрос как прокидывать идентификатор встречи в урл для использования is_opend

    PAGE_URL = Links.MEET_PAGE
    # Вход в конференцию
    ENTER_WITHOUT_CHEKING = ("xpath", "//button[text()='Войти без проверки']")
    ENTER_WITH_CHEKING = ("xpath", "//button[text()='Проверить устройства']")
    # Кнопки внутри конференции
    MICROPHONE_BUTTON = ("xpath", "div[text()='Микрофон']")
    CAMERA_BUTTON = ("xpath", "div[text()='Камера']")
    SHARE_BUTTON = ("xpath", "div[text()='Демонстрация']")
    CHAT_BUTTON = ("xpath", "div[text()='Чат']")
    PARTICIPANTS_BUTTON = ("xpath", "div[text()='Участники']")
    VIEW_BUTTON = ("xpath", "div[text()='Вид']")
    RECORD_BUTTON = ("xpath", "div[text()='Запись']")
    MORE_BUTTON = ("xpath", "div[text()='Ещё']")
    END_BUTTON = ("xpath", "div[text()='Завершить']")

    # Всплывающие уведмоления
    PUSH_ENTER_MEET = ("xpath", "//p[text()='Вы вошли в комнату!']")

    @allure.step("Enter without cheking")
    def click_on_enter_without_cheking_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ENTER_WITHOUT_CHEKING)).click()

    @allure.step("Check push enter meet")
    def check_enter_meet_push(self):
        self.wait.until(EC.visibility_of_element_located(self.PUSH_ENTER_MEET))
        self.wait.until(EC.text_to_be_present_in_element(self.PUSH_ENTER_MEET, "Вы вошли в комнату!"))

    @allure.step("Click on dismiss alert button")
    def click_on_dismiss_alert_button(self):
        time.sleep(2)
        keyboard.press('enter')