import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC



class UsersPage(BasePage):

    PAGE_URL = Links.USERS_PAGE