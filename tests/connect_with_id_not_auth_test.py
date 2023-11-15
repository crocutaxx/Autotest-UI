import allure
from base.base_test import BaseTest

@allure.feature("Schedule Functionality")
class TestConnectToMeetingWithIDNotAuthUser(BaseTest):

    @allure.title("Connect to meeting with id and not auth user")
    @allure.severity("Critical")
    def test_connect_to_meeting_wtih_id_not_auth_user(self,setup_1):
        self.login_page.open()
        self.login_page.click_enter_meet_button()
        self.connect_to_meeting_page.is_opened()
        self.connect_to_meeting_page.enter_meet_identificator()
        self.connect_to_meeting_page.enter_user_name()
        self.connect_to_meeting_page.click_enter_button()
        #self.meet_page.click_on_dismiss_alert_button() # Нужен для локального запуска
        self.meet_page.click_on_enter_without_cheking_button()
        #self.meet_page.click_on_dismiss_alert_button() #Нужен для локального запуска
        self.meet_page.click_on_enter_without_cheking_button()
        self.meet_page.check_enter_meet_push
        self.meet_page.make_screenshot("connect_to_meet_not_auth")