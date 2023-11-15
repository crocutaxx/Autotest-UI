import allure
from base.base_test import BaseTest


@allure.feature("Messages Functionality")
class TestSendMessage(BaseTest):

    @allure.title("Search users")
    @allure.severity("Normal")
    def test_send_message(self, setup_1):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.main_page.click_on_messages_button()
        self.messages_page.is_opened()
        self.messages_page.enter_user_name_in_field()
        self.messages_page.check_result_of_search()
        self.messages_page.click_on_user_dialog()
        self.messages_page.user_chat_is_opdend()
        self.messages_page.enter_message()
        self.messages_page.send_message()
        self.main_page.click_on_user_avatar_button()
        self.main_page.click_on_log_out_button()
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.clear_login()
        self.login_page.enter_login(self.data.LOGIN2)
        self.login_page.clear_password()
        self.login_page.enter_password(self.data.PASSWORD2)
        self.login_page.click_submit_button()
        self.main_page.is_opened()
        self.main_page.click_on_messages_button()
        self.messages_page.check_unread_message()
        self.messages_page.click_on_user_dialog()
        self.messages_page.check_last_message()
