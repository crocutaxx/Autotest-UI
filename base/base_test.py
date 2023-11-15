import pytest
from config.data import Data
# user1
from pages.user1.login_page import LoginPage
from pages.user1.main_page import MainPage
from pages.user1.planning_meet_page import PlanningMeetPage
from pages.user1.calendar_page import CalendarPage
from pages.user1.messages_page import MessagesPage
from pages.user1.users_page import UsersPage
from pages.user1.meet_page import MeetPage
from pages.user1.connect_to_meeting_page import ConnectToMeetingPage
# user2
from pages.user2.login_page_2 import LoginPage
from pages.user2.main_page_2 import MainPage
from pages.user2.planning_meet_page_2 import PlanningMeetPage
from pages.user2.calendar_page_2 import CalendarPage
from pages.user2.messages_page_2 import MessagesPage
from pages.user2.users_page_2 import UsersPage
from pages.user2.meet_page_2 import MeetPage
from pages.user2.connect_to_meeting_page_2 import ConnectToMeetingPage
class BaseTest:

    data: Data
    # user1
    login_page: LoginPage
    main_page: MainPage
    planning_meet_page: PlanningMeetPage
    calendar_page: CalendarPage
    users_page: UsersPage
    messages_page: MessagesPage
    meet_page: MeetPage
    connect_to_meeting_page: ConnectToMeetingPage
    # user2
    login_page_2: LoginPage
    main_page_2: MainPage
    planning_meet_page_2: PlanningMeetPage
    calendar_page_2: CalendarPage
    users_page_2: UsersPage
    messages_page_2: MessagesPage
    meet_page_2: MeetPage
    connect_to_meeting_page_2: ConnectToMeetingPage

    @pytest.fixture()
    def setup_1(self, request, driver_1):
        request.cls.driver = driver_1
        request.cls.data = Data()

        request.cls.login_page = LoginPage(driver_1)
        request.cls.main_page = MainPage(driver_1)
        request.cls.planning_meet_page = PlanningMeetPage(driver_1)
        request.cls.calendar_page = CalendarPage(driver_1)
        request.cls.users_page = UsersPage(driver_1)
        request.cls.messages_page = MessagesPage(driver_1)
        request.cls.meet_page = MeetPage(driver_1)
        request.cls.connect_to_meeting_page = ConnectToMeetingPage(driver_1)

    @pytest.fixture()
    def setup_2(self, request, driver_2):
        request.cls.driver = driver_2
        request.cls.data = Data()

        request.cls.login_page_2 = LoginPage(driver_2)
        request.cls.main_page_2 = MainPage(driver_2)
        request.cls.planning_meet_page_2 = PlanningMeetPage(driver_2)
        request.cls.calendar_page_2 = CalendarPage(driver_2)
        request.cls.users_page_2 = UsersPage(driver_2)
        request.cls.messages_page_2 = MessagesPage(driver_2)
        request.cls.meet_page_2 = MeetPage(driver_2)
        request.cls.connect_to_meeting_page_2 = ConnectToMeetingPage(driver_2)
