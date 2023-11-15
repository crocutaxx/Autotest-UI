import allure
from base.base_test import BaseTest

@allure.feature("Schedule Functionality")
class TestScheduleFeature(BaseTest):
    @allure.title("Create schedule")
    @allure.severity("Critical")
    def test_create_schedule(self, setup_1):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.main_page.click_on_planning_meet_button()
        self.planning_meet_page.is_opened()
        self.planning_meet_page.add_topic()
        self.planning_meet_page.add_meet_password()
        self.planning_meet_page.add_meet_description()
        self.planning_meet_page.save_schedule()
        self.planning_meet_page.topic_name_is_saved()
        self.planning_meet_page.meet_password_is_saved()
        self.planning_meet_page.meet_description_is_saved()
        self.planning_meet_page.make_screenshot("test_create_schedule")

