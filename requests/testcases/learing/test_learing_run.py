import allure
from conftest import http
from common.date2 import date2

@allure.feature("运行成功")
class Test_learing_run():
    @allure.story("运行成功")
    def test_run_success(self):
        path='/api/learning/v3/run'
        date=date2["date2"]
        resp=http.post(path,date)
        assert resp.status_code == 200
        print(resp.json())
        assert resp.json()['ok'] == True
