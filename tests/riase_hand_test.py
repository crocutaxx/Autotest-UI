import allure
from base.base_test import BaseTest
import pytest

@allure.feature("Meet Functionality")
class TestCreateRoomInMeet(BaseTest):
    @pytest.mark.debug
    @allure.title("Raise hand at meet")
    @allure.severity("Normal")
    def test_raise_hand_at_meet(self, setup_1, setup_2):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.connect_to_meeting_page.open()
        self.connect_to_meeting_page.is_opened()
        self.connect_to_meeting_page.enter_meet_identificator()
        self.connect_to_meeting_page.click_enter_button()
        # self.meet_page.click_on_dismiss_alert_button() #Нужен для локального запуска
        self.meet_page.click_on_enter_without_cheking_button()
        # self.meet_page.click_on_dismiss_alert_button() #Нужен для локального запуска
        self.meet_page.click_on_enter_without_cheking_button()
        self.meet_page.check_enter_meet_push()
        # start second user case
        self.login_page_2.open()
        self.login_page_2.click_enter_meet_button()
        self.connect_to_meeting_page_2.is_opened()
        self.connect_to_meeting_page_2.enter_meet_identificator()
        self.connect_to_meeting_page_2.enter_user_name()
        self.connect_to_meeting_page_2.click_enter_button()
        # self.meet_page_2.click_on_dismiss_alert_button() # Нужен для локального запуска
        self.meet_page_2.click_on_enter_without_cheking_button()
        # self.meet_page_2.click_on_dismiss_alert_button() # Нужен для локального запуска
        self.meet_page_2.click_on_enter_without_cheking_button()
        self.meet_page_2.check_enter_meet_push()
        # end second user case
        self.meet_page.click_on_more_button()
        self.meet_page.click_on_raise_hand_button()
        self.meet_page.check_your_reise_hand_push()
        # start second user case
        self.meet_page_2.check_someone_reise_hand_push()
        self.meet_page_2.check_reise_hand_icon()
        self.meet_page_2.click_on_participans_button()
        self.meet_page_2.check_reise_hand_icon_in_users()
        self.meet_page_2.make_screenshot("user_rise_hand")
