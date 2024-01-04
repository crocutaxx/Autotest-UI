import allure
import time
import keyboard
import json
import random
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class MeetPage(BasePage):
    # Решить вопрос как прокидывать идентификатор встречи в урл для использования is_opend

    PAGE_URL = Links.MEET_PAGE
    # Вход в конференцию
    ENTER_WITHOUT_CHECKING = ("xpath", "//button[text()='Войти без проверки']")
    ENTER_WITH_CHECKING = ("xpath", "//button[text()='Проверить устройства']")

    # Кнопки внутри конференции
    MICROPHONE_BUTTON = ("xpath", "//div[text()='Микрофон']")
    CAMERA_BUTTON = ("xpath", "//div[text()='Камера']")
    SHARE_BUTTON = ("xpath", "//div[text()='Демонстрация']")

    # Чат и внутри чата
    CHAT_BUTTON = ("xpath", "//div[text()='Чат']")
    COUNT_UNREAD_MESSAGES = ("xpath", "//div[text()='Чат']//span/span")
    CHAT_WIDGET = ("xpath", "//div[@class='chat-container']")
    MESSAGE_FIELD = ("xpath", "//input[@id='outlined-basic']")
    SEND_MESSAGE_BUTTON = ("xpath", "//button[@type='button']")
    LAST_MESSAGE_IN_CHAT = ("xpath", "(//div[@class='message'])[last()]/p[@class='message-text']")
    LAST_PRIVATE_MESSAGE_IN_CHAT = ("xpath", "//p[@class='message-text']")
    MARK_THAT_MESSAGE_IS_PRIVATE = ("xpath", "//span[text()='(Личное сообщение)']")
    MARK_FOR_WHO_MESSAGE = ("xpath", "//span[@class='message-name']/span")
    CHOICE_USER_DIALOG_BUTTON = ("xpath", "//div[text()='Всем']")
    DIALOG_WIDGET_IS_OPENED = ("xpath", "//ul[@role='listbox']")
    SELECT_USER_IN_DIALOG_MENU = ("xpath", "//ul[@role='listbox']/li[2]")


    # Кнопки внутри участников
    PARTICIPANTS_BUTTON = ("xpath", "//div[text()='Участники']")
    PARTICIPANTS_WIDGET = ("xpath", "//div[@class='call-container']")
    COUNT_PARTICIPANTS_ON_MEET = ("xpath", "//p[contains(text(), 'Участники')]")
    ICON_RAISED_HAND_IN_USERS = ("xpath", "//p[text()='" + BasePage.user_name + "']/*[@class='raise']")
    MORE_USER_BUTTON = ("xpath", "(//div[@class='button more'])[2]")
    END_USER_CALL_BUTTON = ("xpath", "//li[text()='Завершить звонок']")
    USERS_MICROPHONE_IS_OFF = ("xpath", "//p[text()='Test Connect']/following-sibling::div/div[@class='button mic off']")
    USERS_MICROPHONE_IS_ON = ("xpath", "//p[text()='Test Connect']/following-sibling::div/div[@class='button mic on']")
    USERS_CAMERA_IS_OFF = ("xpath", "//p[text()='Test Connect']/following-sibling::div/div[@class='button webcam off']")
    USERS_CAMERA_IS_ON = ("xpath", "//p[text()='Test Connect']/following-sibling::div/div[@class='button webcam on']")


    VIEW_BUTTON = ("xpath", "//div[text()='Вид']")
    RECORD_BUTTON = ("xpath", "//div[text()='Запись']")
    MORE_BUTTON = ("xpath", "//div[text()='Ещё']")
    END_BUTTON = ("xpath", "//div[text()='Завершить']")

    # Кнопки внутри "ЕЩЕ"
    FULL_SCREEN_MODE_BUTTON = ("xpath", "//li[text()='Полноэкранный режим']")
    RAISE_HAND_BUTTON = ("xpath", "//li[text()='Поднять руку']")

    ROOMS_BUTTON = ("xpath", "//li[text()='Комнаты']")
    CREATE_ROOM_BUTTON = ("xpath", "//button[text()='Создать комнату']")
    INPUT_NAME_ROOM_FIELD = ("xpath", "//input[@id='outlined-basic']")
    CREATE_ROOM_MODAL_BUTTON = ("xpath", "(//button[text()='Создать комнату'])[2]")
    CREATED_ROOM = ("xpath", "//p[text()='auto room']")
    CONNECT_TO_ROOM_BUTTON = ("xpath", "(//*[@class='btns'])[2]")
    RETURN_IN_MAIN_ROOM = ("xpath", "//button[text()='Вернуться в основную комнату']")
    CLOSE_ROOM_WIDGET = ("xpath", "(//*[@data-testid='CloseIcon'])[2]")

    INFORMATION_BUTTON = ("xpath", "//li[text()='Информация']")
    IDENTIFIER = ("xpath", "//div[contains(@style, 'margin-top')]/p[2]")
    # Кнопки внутри управления встречей
    MEETING_MANAGEMENT_BUTTON = ("xpath", "//li[text()='Управление встречей']")
    MEETING_MANAGEMENT_WIDGET = ("xpath", "//div[@class='call-container']")
    WAITING_ROOM_SWITCH = ("xpath", "//span[text()='Зал ожидания']")
    BLOCK_ROOM_SWITCH = ("xpath", "//span[text()='Заблокировать сеанс']")
    VISUAL_EFFECTS_BUTTON = ("xpath", "//li[text()='Визуальные эффекты']")
    INVITATION_LINK_BUTTON = ("xpath", "//li[text()='Ссылка для приглашения']")
    SETTINGS_BUTTON = ("xpath", "//li[text()='Настройки']")



    # Всплывающие уведмоления
    PUSH_ENTER_MEET = ("xpath", "//p[text()='Вы вошли в комнату!']")
    PUSH_YOUR_RAISED_HAND = ("xpath", "//p[text()='Вы подняли руку']")
    PUSH_SOMEONE_RAISED_HAND = ("xpath", "//p[@class='text']")
    PUSH_LOWERED_HAND = ("xpath", "//p[text()='Вы опустили руку']")
    PUSH_WAITING_ROOM_SWITCH_STATUS_ON = ("xpath", "//div[text()='Зал ожидания успешно включен']")
    PUSH_BLOCK_ROOM_SWITCH = ("xpath", "//div[text()='Сеанс успешно заблокирован']")
    PUSH_BLOCKED_ROOM = ("xpath", "//p[text()='Встреча заблокирована организатором!']")
    PUSH_USER2_JOINED_TO_ROOM = ("xpath", "//p[text()='Test Connect присоединился к встрече']")

    ICON_RAISED_HAND = ("xpath", "//*[@class='icon raise-hand']")
    COPY_IDENTIFIER_BUTTON = ("xpath", "//button[text()='Скопировать идентификатор встречи']")
    CLOSE_IDENTIFIER_MODAL_WINDOW_BUTTON = ("xpath", "//div[@class='devices-settings']/*[name()='svg'] ")
    MORE_MENU_ITEM = ("xpath", "//ul[@role='menu']")
    ROOMS_WIDGET = ("xpath", "//div[@class='call-container']")
    TEXT_IN_WAITING_ROOM = ("xpath", "//p[@class='hall-text']")
    CONFIRM_END_CALL_BUTTON = ("xpath", "//button[text()='Да']")
    MICROPHONE_OFF_ICON =("xpath", "//div[@class='icon mic-off']")
    CAMERA_OFF_ICON = ("xpath", "//div[@class='icon webcam-off']")
    @allure.step("Enter without cheking")
    def click_on_enter_without_checking_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ENTER_WITHOUT_CHECKING)).click()

    @allure.step("Check push enter meet")
    def check_enter_meet_push(self):
        self.wait.until(EC.visibility_of_element_located(self.PUSH_ENTER_MEET))
        self.wait.until(EC.text_to_be_present_in_element(self.PUSH_ENTER_MEET, "Вы вошли в комнату!"))

    @allure.step("Click on dismiss alert button")
    def click_on_dismiss_alert_button(self):
        # alert = self.wait.until(EC.alert_is_present())
        # alert.text == "Вас исключили из встречи"
        # alert.accept()
        time.sleep(2)
        keyboard.press('enter')

    @allure.step("Click on microphone button")
    def click_on_microphone_button(self):
        self.wait.until(EC.visibility_of_element_located(self.MICROPHONE_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.MICROPHONE_BUTTON)).click()

    @allure.step("Click off microphone button")
    def click_off_microphone_button(self):
        self.wait.until(EC.visibility_of_element_located(self.MICROPHONE_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.MICROPHONE_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.MICROPHONE_OFF_ICON))
    @allure.step("User's Microphone is off")
    def users_microphone_is_off(self):
        self.wait.until(EC.visibility_of_element_located(self.USERS_MICROPHONE_IS_OFF))

    @allure.step("User's Microphone is on")
    def users_microphone_is_on(self):
        self.wait.until(EC.visibility_of_element_located(self.USERS_MICROPHONE_IS_ON))
    @allure.step("Click on camera button")
    def click_on_camera_button(self):
        self.wait.until(EC.visibility_of_element_located(self.CAMERA_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.CAMERA_BUTTON)).click()


    @allure.step("Click off camera button")
    def click_off_camera_button(self):
        self.wait.until(EC.visibility_of_element_located(self.CAMERA_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.CAMERA_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.CAMERA_OFF_ICON))

    @allure.step("Camera is off")
    def users_camera_is_off(self):
        self.wait.until(EC.visibility_of_element_located(self.USERS_CAMERA_IS_OFF))

    @allure.step("Camera is on")
    def users_camera_is_on(self):
        self.wait.until(EC.visibility_of_element_located(self.USERS_CAMERA_IS_ON))

    @allure.step("Click on More button")
    def click_on_more_button(self):
        self.wait.until(EC.visibility_of_element_located(self.MORE_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.MORE_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.MORE_MENU_ITEM))

    @allure.step("Click on rooms button")
    def click_on_rooms_button(self):
        self.wait.until(EC.visibility_of_element_located(self.MORE_MENU_ITEM))
        self.wait.until(EC.element_to_be_clickable(self.ROOMS_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.ROOMS_WIDGET))

    @allure.step("Click on create room button")
    def click_on_create_room_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_ROOM_BUTTON)).click()

    @allure.step("Enter name room in field")
    def enter_room_name(self):
        self.wait.until(EC.element_to_be_clickable(self.INPUT_NAME_ROOM_FIELD)).send_keys("auto room")

    @allure.step("Click on modal create room button")
    def click_on_modal_create_room_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_ROOM_MODAL_BUTTON)).click()

    @allure.step("Check created room")
    def check_created_room(self):
        self.wait.until(EC.visibility_of_element_located(self.CREATED_ROOM))
        self.wait.until(EC.text_to_be_present_in_element(self.CREATED_ROOM, "auto room"))

    @allure.step("Click on raise hand button")
    def click_on_raise_hand_button(self):
        self.wait.until(EC.visibility_of_element_located(self.RAISE_HAND_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.RAISE_HAND_BUTTON)).click()

    @allure.step("Check your rise hand push")
    def check_your_raised_hand_push(self):
        self.wait.until(EC.visibility_of_element_located(self.PUSH_YOUR_RAISED_HAND))
        self.wait.until(EC.text_to_be_present_in_element(self.PUSH_YOUR_RAISED_HAND, "Вы подняли руку"))

    @allure.step("Check someone rise hand push")
    def check_someone_raised_hand_push(self):
        self.wait.until(EC.visibility_of_element_located(self.PUSH_SOMEONE_RAISED_HAND))
        self.wait.until(EC.text_to_be_present_in_element(self.PUSH_SOMEONE_RAISED_HAND, f"{BasePage.user_name} поднял руку"))

    @allure.step("Check rise hand icon")
    def check_raised_hand_icon(self):
        self.wait.until(EC.visibility_of_element_located(self.ICON_RAISED_HAND))

    @allure.step("Click on participants button")
    def click_on_participants_button(self):
        self.wait.until(EC.element_to_be_clickable(self.PARTICIPANTS_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.PARTICIPANTS_WIDGET))
    @allure.step("Check rise hand icon in users")
    def check_raised_hand_icon_in_users(self):
        self.wait.until(EC.visibility_of_element_located(self.ICON_RAISED_HAND_IN_USERS))

    @allure.step("Click on connect to room button")
    def click_on_connect_to_room_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CONNECT_TO_ROOM_BUTTON)).click()

    @allure.step("Check connect to room")
    def check_return_to_main_room_button(self):
        self.wait.until(EC.visibility_of_element_located(self.RETURN_IN_MAIN_ROOM))

    @allure.step("Click on return to main room button")
    def click_on_return_to_main_room_button(self):
        self.wait.until(EC.visibility_of_element_located(self.RETURN_IN_MAIN_ROOM))
        self.wait.until(EC.element_to_be_clickable(self.RETURN_IN_MAIN_ROOM)).click()

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

    @allure.step("Click on copy identifier button")
    def get_identifier_from_information_window(self):
        meeting_id_text = self.wait.until(EC.visibility_of_element_located(self.IDENTIFIER)).text
        meeting_id = meeting_id_text
        data = {"meeting_id": meeting_id}

        with open("data/tests_data.json", "w") as json_file:
            json.dump(data, json_file)

    @allure.step("Click close information window button")
    def click_close_information_window_button(self):
        self.wait.until(EC.visibility_of_element_located(self.CLOSE_IDENTIFIER_MODAL_WINDOW_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.CLOSE_IDENTIFIER_MODAL_WINDOW_BUTTON)).click()

    @allure.step("Close room widget")
    def close_room_widget(self):
        self.wait.until(EC.element_to_be_clickable(self.CLOSE_ROOM_WIDGET)).click()

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
        if alert.text == "Вас исключили из встречи":
            alert.accept()

    @allure.step("Click on chat button")
    def click_on_chat_button(self):
        self.wait.until(EC.visibility_of_element_located(self.CHAT_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.CHAT_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.CHAT_WIDGET))

    @allure.step("Enter message")
    def enter_message_in_field(self):
        message_field = self.wait.until(EC.element_to_be_clickable(self.MESSAGE_FIELD))
        new_message = "message123, hello че кого?"
        message_field.send_keys(new_message)

    @allure.step("Click on send message button")
    def click_on_send_message_button(self):
        self.wait.until(EC.visibility_of_element_located(self.SEND_MESSAGE_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.SEND_MESSAGE_BUTTON)).click()

    @allure.step("Check count unread messages")
    def check_count_of_unread_messages(self):
        self.wait.until(EC.visibility_of_element_located(self.COUNT_UNREAD_MESSAGES))
        self.wait.until(EC.text_to_be_present_in_element(self.COUNT_UNREAD_MESSAGES, "1"))

    @allure.step("Check last message in chat")
    def check_last_message_in_chat(self):
        self.wait.until(EC.visibility_of_element_located(self.LAST_MESSAGE_IN_CHAT))
        self.wait.until(EC.text_to_be_present_in_element(self.LAST_MESSAGE_IN_CHAT, "message123, hello че кого?"))

    @allure.step("Click on user dialog button")
    def click_on_user_dialog_button(self):
        self.wait.until(EC.visibility_of_element_located(self.CHOICE_USER_DIALOG_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.CHOICE_USER_DIALOG_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.DIALOG_WIDGET_IS_OPENED))

    @allure.step("Select user in dialog menu")
    def select_user_in_dialog_menu(self):
        self.wait.until(EC.visibility_of_element_located(self.SELECT_USER_IN_DIALOG_MENU))
        self.wait.until(EC.element_to_be_clickable(self.SELECT_USER_IN_DIALOG_MENU)).click()

    @allure.step("Check last message in chat")
    def check_last_private_message_in_chat(self):
        self.wait.until(EC.visibility_of_element_located(self.LAST_PRIVATE_MESSAGE_IN_CHAT))
        self.wait.until(EC.text_to_be_present_in_element(self.MARK_THAT_MESSAGE_IS_PRIVATE, "(Личное сообщение)"))
        self.wait.until(EC.text_to_be_present_in_element(self.MARK_FOR_WHO_MESSAGE, "кому Test Connect"))
        self.wait.until(EC.text_to_be_present_in_element(self.LAST_PRIVATE_MESSAGE_IN_CHAT, "message123, hello че кого?"))

    @allure.step("Click on management button")
    def click_on_management_button(self):
        self.wait.until(EC.visibility_of_element_located(self.MEETING_MANAGEMENT_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.MEETING_MANAGEMENT_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.MEETING_MANAGEMENT_WIDGET))

    @allure.step("On switch waiting room")
    def switch_waiting_room_on(self):
        self.wait.until(EC.element_to_be_clickable(self.WAITING_ROOM_SWITCH)).click()
        self.wait.until(EC.visibility_of_element_located(self.PUSH_WAITING_ROOM_SWITCH_STATUS_ON))

    @allure.step("Check text in waiting room")
    def check_text_in_waiting_room(self):
        self.wait.until(EC.visibility_of_element_located(self.TEXT_IN_WAITING_ROOM))
        self.wait.until(EC.text_to_be_present_in_element(self.TEXT_IN_WAITING_ROOM,
                                                         "Пожалуйста подождите, организатор встречи скоро разрешит вам войти"))

    @allure.step("On switch for block room")
    def switch_blocking_room_on(self):
        self.wait.until(EC.element_to_be_clickable(self.BLOCK_ROOM_SWITCH)).click()
        self.wait.until(EC.visibility_of_element_located(self.PUSH_BLOCK_ROOM_SWITCH))

    @allure.step("Check push in blocked room")
    def check_push_in_blocked_room(self):
        self.wait.until(EC.visibility_of_element_located(self.PUSH_BLOCKED_ROOM))
        self.wait.until(EC.text_to_be_present_in_element(self.PUSH_BLOCKED_ROOM,
                                                         "Встреча заблокирована организатором!"))

    @allure.step("Check push user joined to room")
    def check_push_user_joined_to_room(self):
        self.wait.until(EC.visibility_of_element_located(self.PUSH_USER2_JOINED_TO_ROOM))
        self.wait.until(EC.text_to_be_present_in_element(self.PUSH_USER2_JOINED_TO_ROOM,
                                                         "Test Connect присоединился к встрече"))
    @allure.step("Click on end call button")
    def click_on_end_call_button(self):
        self.wait.until(EC.visibility_of_element_located(self.END_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.END_BUTTON)).click()

    @allure.step("Click on confirm end call button")
    def click_on_confirm_end_call_button(self):
        self.wait.until(EC.visibility_of_element_located(self.CONFIRM_END_CALL_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_END_CALL_BUTTON)).click()