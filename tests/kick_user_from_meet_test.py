import allure
from base.base_test import BaseTest


@allure.feature("Meet Functionality")
class TestKickUserFromMeet(BaseTest):


    @allure.title("Kick user from meet")
    @allure.severity("Normal")
    def test_kick_user_from_meet(self, setup_1, setup_2):
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
        self.meet_page.click_on_participans_button()
        self.meet_page.click_on_more_user_button()
        self.meet_page.click_on_end_call_user_button()
        self.meet_page.check_count_of_participants()

        # start second user case
        self.meet_page_2.check_and_accept_alert()
        self.meet_page_2.make_screenshot("kick_user")
