from common.commonDate import CommonDate
from conftest import http
import allure

@allure.feature("登录成功")
class Test_login():
    @allure.story("登录成功")
    def test_login_success(self):
        path = '/api/auth/login'
        date = {'loginId': CommonDate.mobile,
                'password': CommonDate.password,
                'orgId': CommonDate.orgId}
        resp = http.post(path, date)
        assert resp.status_code == 200
        assert resp.json()['ok']==True

    @allure.story("登录失败")
    def test_login_fail(self):
        path = '/api/auth/login'
        date = {'loginId': '111',
                'password': CommonDate.password,
                'orgId': 22}
        resp = http.post(path, date)

        # assert resp.status_code == 301
        assert resp.json()['ok'] == False




    # @allure.story("用户不存在")
    # def test_login_fail(self):
    #     path = '/api/auth/login'
    #     date = {'username': '999',
    #             'password': CommonDate.password,
    #             'orgId': CommonDate.orgId}
    #     resp = http.post(path, date)
    #     assert resp.status_code == 301
    #     # assert resp['msg']=='用户不存在'
    #
    # @allure.story("用户密码错误")
    # def test_login_fail(self):
    #     path = '/api/auth/login'
    #     date = {'username': CommonDate.mobile,
    #             'password': '555',
    #             'orgId': CommonDate.orgId}
    #     resp = http.post(path, date)
    #     assert resp.status_code == 401
    #     # assert resp['msg'] == '用户密码错误'
    #
    # @allure.story("此账户禁止登录")
    # def test_login_fail(self):
    #     path = '/api/auth/login'
    #     date = {'username': '',
    #             'password': '',
    #             'orgId': CommonDate.orgId}
    #     resp = http.post(path, date)
    #     assert resp.status_code == 3010
    #     # assert resp['msg'] == '此账户禁止登录'
    #
    # @allure.story("用户不存在")
    # def test_login_fail(self):
    #     path = '/api/auth/login'
    #     date = {'password': CommonDate.password,
    #             'orgId': CommonDate.orgId}
    #     resp = http.post(path, date)
    #     assert resp.status_code == 301
    #     # assert resp['msg'] == '用户不存在'
