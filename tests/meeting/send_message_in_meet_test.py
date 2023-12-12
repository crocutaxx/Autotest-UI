import allure
from base.base_test import BaseTest
import pytest

@allure.feature("Meet Functionality")
class TestSendMessageInMeet(BaseTest):


    @allure.title("send message in meet")
    @allure.severity("Normal")
    def test_send_messge_in_meet(self, user_1, user_2):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.connect_to_meeting_page.open()
        self.connect_to_meeting_page.is_opened()
        self.connect_to_meeting_page.enter_meet_identifier()
        self.connect_to_meeting_page.click_enter_button()
        # self.meet_page.click_on_dismiss_alert_button() #Нужен для локального запуска
        self.meet_page.click_on_enter_without_checking_button()
        # self.meet_page.click_on_dismiss_alert_button() #Нужен для локального запуска
        self.meet_page.click_on_enter_without_checking_button()
        self.meet_page.check_enter_meet_push()
        # start second user case
        self.login_page_2.open()
        self.login_page_2.click_enter_meet_button()
        self.connect_to_meeting_page_2.is_opened()
        self.connect_to_meeting_page_2.enter_meet_identifier()
        self.connect_to_meeting_page_2.enter_user_name()
        self.connect_to_meeting_page_2.click_enter_button()
        # self.meet_page_2.click_on_dismiss_alert_button() # Нужен для локального запуска
        self.meet_page_2.click_on_enter_without_checking_button()
        # self.meet_page_2.click_on_dismiss_alert_button() # Нужен для локального запуска
        self.meet_page_2.click_on_enter_without_checking_button()
        self.meet_page_2.check_enter_meet_push()
        # end second user case
        self.meet_page.click_on_chat_button()
        self.meet_page.enter_message_in_field()
        self.meet_page.click_on_send_message_button()
        # start second user case
        self.meet_page_2.check_count_of_unread_messages()
        self.meet_page_2.click_on_chat_button()
        self.meet_page_2.check_last_message_in_chat()
        self.meet_page_2.make_screenshot("message_for_all")
