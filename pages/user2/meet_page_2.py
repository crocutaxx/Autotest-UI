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
    MICROPHONE_BUTTON = ("xpath", "//div[text()='Микрофон']")
    CAMERA_BUTTON = ("xpath", "//div[text()='Камера']")
    SHARE_BUTTON = ("xpath", "//div[text()='Демонстрация']")
    CHAT_BUTTON = ("xpath", "//div[text()='Чат']")

    # Кнопки внутри участников
    PARTICIPANTS_BUTTON = ("xpath", "//div[text()='Участники']")
    COUNT_PARTICIPANTS_ON_MEET = ("xpath", "//p[contains(text(), 'Участники')]")
    ICON_RISE_HAND_IN_USERS = ("xpath", "//p[text()='Тестирование']/*[@class='raise']")
    MORE_USER_BUTTON = ("xpath", "(//div[@class='button more'])[2]")
    END_USER_CALL_BUTTON = ("xpath", "//li[text()='Завершить звонок']")

    VIEW_BUTTON = ("xpath", "//div[text()='Вид']")
    RECORD_BUTTON = ("xpath", "//div[text()='Запись']")
    MORE_BUTTON = ("xpath", "//div[text()='Ещё']")
    END_BUTTON = ("xpath", "//div[text()='Завершить']")

    # Кнопки внутри "ЕЩЕ"
    FULL_SCREAN_MODE_BUTTON = ("xpath", "//li[text()='Полноэкранный режим']")
    RAISE_HAND_BUTTON = ("xpath", "//li[text()='Поднять руку']")

    ROOMS_BUTTON = ("xpath", "//li[text()='Комнаты']")
    CREATE_ROOM_BUTTON = ("xpath", "//button[text()='Создать комнату']")
    INPUT_NAME_ROOM_FIELD = ("xpath", "//input[@id='outlined-basic']")
    CREATE_ROOM_MODAL_BUTTON = ("xpath", "(//button[text()='Создать комнату'])[2]")
    CREATED_ROOM = ("xpath", "//p[text()='auto room']")
    CONNECT_TO_ROOM_BUTTON = ("xpath", "(//*[@class='btns'])[2]")
    RETURN_IN_MAIN_ROOM = ("xpath", "//button[text()='Вернуться в основную комнату']")
    CLOSE_ROOM_VIDGET =("xpath", "(//*[@data-testid='CloseIcon'])[2]")

    INFORMATION_BUTTON = ("xpath", "//li[text()='Информация']")
    MEETING_MANAGEMENT_BUTTON = ("xpath", "//li[text()='Управление встречей']")
    VISUAL_EFFECTS_BUTTON = ("xpath", "//li[text()='Визуальные эффекты']")
    INVITATION_LINK_BUTTON = ("xpath", "//li[text()='Ссылка для приглашения']")
    SETTINGS_BUTTON = ("xpath", "//li[text()='Настройки']")



    # Всплывающие уведмоления
    PUSH_ENTER_MEET = ("xpath", "//p[text()='Вы вошли в комнату!']")
    PUSH_YOUR_RISE_HAND = ("xpath", "//p[text()='Вы подняли руку']")
    PUSH_SOMEONE_RISE_HAND = ("xpath", "//p[@class='text']")
    PUSH_LOWERED_HAND = ("xpath", "//p[text()='Вы опустили руку']")

    ICON_RISE_HAND = ("xpath", "//*[@class='icon raise-hand']")
    COPY_IDENTIFICATOR_BUTTON = ("xpath", "//button[text()='Скопировать идентификатор встречи']")
    CLOSE_INFORMATIOM_MODAL_WINDOW_BUTTON = ("xpath", "//div[@class='devices-settings']/*[name()='svg'] ")
    MORE_MENU_ITEM = ("xpath", "//ul[@role='menu']")
    ROOMS_VIDGET = ("xpath", "//div[@class='call-container']")
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

    @allure.step("Click on More button")
    def click_on_more_button(self):
        self.wait.until(EC.visibility_of_element_located(self.MORE_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.MORE_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.MORE_MENU_ITEM))

    @allure.step("Click on rooms button")
    def click_on_rooms_button(self):
        self.wait.until(EC.visibility_of_element_located(self.MORE_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.ROOMS_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.ROOMS_VIDGET))

    @allure.step("Click on create room button")
    def click_on_create_room_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_ROOM_BUTTON)).click()

    @allure.step("Enter name room in field")
    def enter_room_name(self):
        self.wait.until(EC.element_to_be_clickable(self.INPUT_NAME_ROOM_FIELD)).send_keys("auto room")

    @allure.step("Click on modal create room button")
    def click_on_modal_create_room_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_ROOM_MODAL_BUTTON)).click()

    @allure.step("Check created romm")
    def check_created_room(self):
        self.wait.until(EC.visibility_of_element_located(self.CREATED_ROOM))
        self.wait.until(EC.text_to_be_present_in_element(self.CREATED_ROOM, "auto room"))

    @allure.step("Click on raise hand button")
    def click_on_raise_hand_button(self):
        self.wait.until(EC.element_to_be_clickable(self.RAISE_HAND_BUTTON)).click()

    @allure.step("Check your rise hand push")
    def check_your_reise_hand_push(self):
        self.wait.until(EC.visibility_of_element_located(self.PUSH_YOUR_RISE_HAND))
        self.wait.until(EC.text_to_be_present_in_element(self.PUSH_YOUR_RISE_HAND, "Вы подняли руку"))

    @allure.step("Check someone rise hand push")
    def check_someone_reise_hand_push(self):
        self.wait.until(EC.visibility_of_element_located(self.PUSH_SOMEONE_RISE_HAND))
        self.wait.until(EC.text_to_be_present_in_element(self.PUSH_SOMEONE_RISE_HAND, "Тестирование поднял руку"))

    @allure.step("Check rise hand icon")
    def check_reise_hand_icon(self):
        self.wait.until(EC.visibility_of_element_located(self.ICON_RISE_HAND))

    @allure.step("Click on participans button")
    def click_on_participans_button(self):
        self.wait.until(EC.element_to_be_clickable(self.PARTICIPANTS_BUTTON)).click()

    @allure.step("Check rise hand icon in users")
    def check_reise_hand_icon_in_users(self):
        self.wait.until(EC.visibility_of_element_located(self.ICON_RISE_HAND_IN_USERS))

    @allure.step("Click on connect to room button")
    def click_on_connect_to_toom_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CONNECT_TO_ROOM_BUTTON)).click()

    @allure.step("Check connect to room")
    def check_return_to_main_room_button(self):
        self.wait.until(EC.visibility_of_element_located(self.RETURN_IN_MAIN_ROOM))

    @allure.step("Check count of participants")
    def check_count_of_participants(self):
        self.wait.until(EC.visibility_of_element_located(self.COUNT_PARTICIPANTS_ON_MEET))
        self.wait.until(EC.text_to_be_present_in_element(self.COUNT_PARTICIPANTS_ON_MEET, "Участники (1)"))

    @allure.step("Click on invitation link button")
    def click_on_invitation_link_button(self):
        self.wait.until(EC.visibility_of_element_located(self.INVITATION_LINK_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.INVITATION_LINK_BUTTON)).click()

    @allure.step("Click on information button")
    def click_on_information_button(self):
        self.wait.until(EC.visibility_of_element_located(self.INFORMATION_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.INFORMATION_BUTTON)).click()

    @allure.step("Click on copy identificator button")
    def click_on_copy_identificator_button(self):
        self.wait.until(EC.visibility_of_element_located(self.COPY_IDENTIFICATOR_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.COPY_IDENTIFICATOR_BUTTON)).click()

    @allure.step("Click close inwormation window button")
    def click_close_information_window_button(self):
        self.wait.until(EC.visibility_of_element_located(self.CLOSE_INFORMATIOM_MODAL_WINDOW_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.CLOSE_INFORMATIOM_MODAL_WINDOW_BUTTON)).click()

    @allure.step("Close room vidget")
    def close_room_vidget(self):
        self.wait.until(EC.element_to_be_clickable(self.CLOSE_ROOM_VIDGET)).click()

    @allure.step("Click on more user button")
    def click_on_more_user_button(self):
        self.wait.until(EC.element_to_be_clickable(self.MORE_USER_BUTTON)).click()

    @allure.step("Click on end call user button")
    def click_on_end_call_user_button(self):
        self.wait.until(EC.visibility_of_element_located(self.END_USER_CALL_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.END_USER_CALL_BUTTON)).click()
    @allure.step("Accept alert kick")
    def check_and_accept_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        alert.text == "Вас исключили из встречи"
        alert.accept()