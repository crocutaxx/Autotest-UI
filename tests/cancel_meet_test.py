import allure
from base.base_test import BaseTest


@allure.feature("Schedule Functionality")
class TestScheduleBlok(BaseTest):

    @allure.title("Blok schedule")
    @allure.severity("Normal")
    def test_blok_schedule(self, setup_1):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.main_page.click_on_planning_meet_button()
        self.planning_meet_page.is_opened()
        self.planning_meet_page.add_topic()
        self.planning_meet_page.save_schedule()
        self.main_page.open()
        self.main_page.click_on_planned_name_meet()
        self.main_page.click_on_cancell_meet_button()
        self.main_page.click_on_confirm_action_button()
        self.main_page.check_push_meet_cancel()
        self.main_page.click_on_canceled_name_meet()
        self.main_page.meet_is_canceled()
        self.main_page.make_screenshot("test_cancel_meet")
        self.main_page.click_on_delete_meet_button()
        self.main_page.click_on_confirm_action_button()


