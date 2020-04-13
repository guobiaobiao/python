import pytest
import time
from selenium.webdriver.common.keys import Keys

class TestBaiDuSearch:

    @pytest.mark.usefixtures('browser')
    def test_search(self, browser):
        browser.get("https://www.baidu.com")
        elment=browser.find_element_by_id('kw')
        elment.send_keys('selenium'+Keys.ENTER)
        time.sleep(5)




