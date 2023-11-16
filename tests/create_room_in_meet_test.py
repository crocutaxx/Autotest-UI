import allure
from base.base_test import BaseTest


@allure.feature("Meet Functionality")
class TestCreateRoomInMeet(BaseTest):

    @allure.title("Create room in meet")
    @allure.severity("Normal")
    def test_create_room_in_meet(self, setup_1):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.main_page.click_on_new_meet_button()
        # self.meet_page.is_opened() Разобраться с идентификатором комант
        # self.meet_page.click_on_dismiss_alert_button() # Нужен для локального запуска
        self.meet_page.click_on_enter_without_cheking_button()
        self.meet_page.check_enter_meet_push()
        self.meet_page.click_on_more_button()
        self.meet_page.click_on_rooms_button()
        self.meet_page.click_on_create_room_button()
        self.meet_page.enter_room_name()
        self.meet_page.click_on_modal_create_room_button()
        self.meet_page.check_created_room()
        self.meet_page.make_screenshot("created_room")
