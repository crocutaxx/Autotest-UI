import allure
from base.base_test import BaseTest

@allure.feature("Schedule Functionality")
class TestConnectToMeetingWithIDAuthUser(BaseTest):

    @allure.title("Connect to meeting with id and auth user")
    @allure.severity("Critical")
    def test_connect_to_meeting_wtih_id_auth_user(self,setup_1):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.connect_to_meeting_page.open()
        self.connect_to_meeting_page.is_opened()
        self.connect_to_meeting_page.enter_meet_identificator()
        self.connect_to_meeting_page.click_enter_button()
        #self.meet_page.click_on_dismiss_alert_button() #Нужен для локального запуска
        self.meet_page.click_on_enter_without_cheking_button()
        #self.meet_page.click_on_dismiss_alert_button() #Нужен для локального запуска
        self.meet_page.click_on_enter_without_cheking_button()
        self.meet_page.check_enter_meet_push