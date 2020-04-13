import allure
from conftest import http
from common.date3 import date3

@allure.feature("提交成功")
class Test_learing_judge():
    @allure.story("提交成功")
    def test_judge_success(self):
        path='/api/learning/v3/judge'
        date=date3["date3"]
        resp=http.post(path,date)
        assert resp.status_code == 200
        print(resp.json)
        # assert resp.json()['ok'] == True
