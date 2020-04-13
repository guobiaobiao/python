import allure
from conftest import http
from common.date1 import date1

@allure.feature("时间响应成功")
class Test_learing_time():
    @allure.story("时间响应成功")
    def test_time_success(self):
        path='/api/record/recordStudyTime/'
        date=date1["date1"]
        resp=http.post(path,date)
        assert resp.status_code == 200
        print(resp.json())
        # assert resp.json()['ok'] == True
