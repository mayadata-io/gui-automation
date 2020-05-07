from selenium.webdriver.common.by import By
from main.pages.BasePage import BasePage, EMPTY_CARD_CONTAINER


class MonitorPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
