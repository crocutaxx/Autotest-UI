from selenium import webdriver

class Links():


    HOST = "https://dev.qosyl.kz"
    LOGIN_PAGE = f"{HOST}/login"
    MAIN_PAGE = f"https://dev.qosyl.kz/"
    PLANNING_MEET_PAGE = f"{HOST}/schedule"
    CALENDAR_PAGE = f"{HOST}/calendar"
    USERS_PAGE = f"{HOST}/users"
    MESSAGES_PAGE = f"{HOST}/messages"
    MEET_PAGE = f"{HOST}/meeting/?room="