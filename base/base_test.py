import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.planning_meet_page import PlanningMeetPage
from pages.calendar_page import CalendarPage
from pages.messages_page import MessagesPage
from pages.users_page import UsersPage
from pages.meet_page import MeetPage

class BaseTest:

    data: Data

    login_page: LoginPage
    main_page: MainPage
    planning_meet_page: PlanningMeetPage
    calendar_page: CalendarPage
    users_page: UsersPage
    messages_page: MessagesPage
    meet_page: MeetPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.login_page = LoginPage(driver)
        request.cls.main_page = MainPage(driver)
        request.cls.planning_meet_page = PlanningMeetPage(driver)
        request.cls.calendar_page = CalendarPage(driver)
        request.cls.users_page = UsersPage(driver)
        request.cls.messages_page = MessagesPage(driver)
        request.cls.meet_page = MeetPage(driver)