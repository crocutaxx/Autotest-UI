import allure
from base.base_test import BaseTest

@allure.feature("Connect to meeting Functionality")
class TestConnectingUsersToMeetingWithID(BaseTest):

    @allure.title("Connecting to a meeting via the meeting ID as an unauthorized user")
    @allure.severity("Critical")
    def test_connecting_to_meeting_wtih_id_unauth_user(self, user_1):
        self.login_page.open()
        self.login_page.click_enter_meet_button()
        self.connect_to_meeting_page.is_opened()
        self.connect_to_meeting_page.enter_meet_identifier()
        self.connect_to_meeting_page.enter_user_name()
        self.connect_to_meeting_page.click_enter_button()
        #self.meet_page.click_on_dismiss_alert_button() # Нужен для локального запуска
        self.meet_page.click_on_enter_without_checking_button()
        #self.meet_page.click_on_dismiss_alert_button() #Нужен для локального запуска
        self.meet_page.click_on_enter_without_checking_button()
        self.meet_page.check_enter_meet_push
        self.meet_page.make_screenshot("connect_to_meet_unauth")

    @allure.title("Connecting to a meeting via the meeting ID as an authorized user")
    @allure.severity("Critical")
    def test_connecting_to_meeting_wtih_id_auth_user(self, user_1):
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
        self.meet_page.check_enter_meet_push
        self.meet_page.make_screenshot("connect_to_meet_auth")