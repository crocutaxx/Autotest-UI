import allure
from base.base_test import BaseTest
import pytest
import time

@allure.feature("Meet Functionality")
class TestStatusCameraAndMicrophone(BaseTest):


    @allure.title("Status camera adn microphone in meet")
    @allure.severity("Normal")
    def test_status_camera_and_microphone(self, user_1, user_2):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.connect_to_meeting_page.open()
        self.connect_to_meeting_page.is_opened()
        self.connect_to_meeting_page.enter_meet_identifier()
        self.connect_to_meeting_page.click_enter_button()
        self.meet_page.click_on_enter_without_checking_button()
        # self.meet_page.click_on_dismiss_alert_button() #Нужен для локального запуска
        self.meet_page.click_on_enter_without_checking_button()
        self.meet_page.check_enter_meet_push()

        self.login_page_2.open()
        self.login_page_2.click_enter_meet_button()
        self.connect_to_meeting_page_2.is_opened()
        self.connect_to_meeting_page_2.enter_meet_identifier()
        self.connect_to_meeting_page_2.enter_user_name()
        self.connect_to_meeting_page_2.click_enter_button()
        self.meet_page_2.click_on_enter_without_checking_button()
        # self.meet_page_2.click_on_dismiss_alert_button() # Нужен для локального запуска
        self.meet_page_2.click_on_enter_without_checking_button()
        self.meet_page_2.check_enter_meet_push()
        self.meet_page_2.click_on_microphone_button()
        self.meet_page_2.click_on_camera_button()

        self.meet_page.click_on_participants_button()
        self.meet_page.users_microphone_is_on()
        self.meet_page.users_camera_is_on()
        self.meet_page.make_screenshot("camera_and_microphone_is_on")

        self.meet_page_2.click_off_camera_button()
        self.meet_page_2.click_off_microphone_button()

        self.meet_page.users_camera_is_off()
        self.meet_page.users_microphone_is_off()
        self.meet_page.make_screenshot("status_camera_and_microphone")
