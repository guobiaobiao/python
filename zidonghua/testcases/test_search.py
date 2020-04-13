import allure
from pages.home_page import HomePage
import time

class TestBaiduSerch:

    @allure.feature("用户功能")

    @allure.story("百度搜索")
    def test_baidu_search_case(self,browser,base_url):
        page=HomePage(browser)
        page.open(base_url)
        page.search("pytest")
        time.sleep(3)

    @allure.story("百度搜索设置")
    def test_baidu_search_setting(self,browser):
        pass