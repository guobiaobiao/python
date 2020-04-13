from base.base import BasePage
from base.logger import Logger

logger=Logger(logger="HomePage").getlog()

class HomePage(BasePage):

    # locators
    _search_input="kw"
    _search_button="su"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def enter_search(self,content):
        self.element_send_keys(self._search_input,content,"id")

    def click_search_button(self):
        self.element_click(self._search_button,"id")

    def search(self,content):
        self.enter_search(content)
        self.click_search_button()