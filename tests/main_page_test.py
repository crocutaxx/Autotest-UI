import allure
from base.base_test import BaseTest

@allure.feature("Main page functionality")
class TestMainPage(BaseTest):


    @allure.title("Starting new meeting")
    @allure.severity("Critical")
    def test_starting_new_meeting(self, user_1):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.main_page.click_on_new_meet_button()
        # self.meet_page.is_opened() Разобраться с идентификатором комант
        # self.meet_page.click_on_dismiss_alert_button() # Нужен для локального запуска
        self.meet_page.click_on_enter_without_checking_button()
        self.meet_page.check_enter_meet_push()
        self.meet_page.make_screenshot("The meeting is starting")


    @allure.title("The test of opening the meeting planning page")
    @allure.severity("Normal")
    def test_switching_to_meeting_planning(self, user_1):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.main_page.click_on_planning_meet_button()
        self.planning_meet_page.is_opened()
        self.planning_meet_page.make_screenshot("The planning meet page is opend")

    @allure.title("The test of opening the calendar page")
    @allure.severity("Normal")
    def test_switching_to_calendar(self, user_1):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.main_page.click_on_calendar_button()
        self.calendar_page.is_opened()
        self.calendar_page.make_screenshot("The calendar page is opend")


    @allure.title("Switching to messages from main page")
    @allure.severity("Normal")
    def test_switching_to_messages(self, user_1):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.main_page.click_on_messages_button()
        self.messages_page.is_opened()
        self.messages_page.make_screenshot("Message page is opend")
