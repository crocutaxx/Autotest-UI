import allure
from base.base_test import BaseTest
import pytest

@allure.feature("Meet Functionality")
class TestEndCallMeet(BaseTest):


    @allure.title("End call on meet")
    @allure.severity("Critical")
    def test_end_call_on_meet(self, user_1, user_2):
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

        self.meet_page.click_on_end_call_button()
        self.meet_page.click_on_confirm_end_call_button()
        self.connect_to_meeting_page.is_opened()
        self.connect_to_meeting_page.make_screenshot("End_Call")
        self.meet_page_2.click_on_participants_button()
        self.meet_page_2.check_count_of_participants()


