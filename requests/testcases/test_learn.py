from conftest import http
import allure

@allure.feature("查看学习")
class Test_leaen():
    @allure.story("查看学习动态成功")
    def test_trends(self):
        path='/api/courses/v3/trends'
        resp=http.get(path)
        assert resp.status_code==200
        assert resp.json()['ok'] == True

    @allure.story("获取课程列表")
    def test_myCourses(self):
        path = '/api/courses/v3/myCourses'
        resp = http.get(path)
        assert resp.status_code == 200
        assert resp.json()['ok'] == True

    @allure.story("获取最近学习小节")
    def test_recentLesson(self):
        path = '/api/learning/v3/114/recentLesson'
        resp = http.get(path)
        assert resp.status_code == 200
        assert resp.json()['ok'] == True

    @allure.story("获取课程角色")
    def test_courseRole(self):
        path = '/api/courses/v3/114/courseRole/'
        resp = http.get(path)
        assert resp.status_code == 200
        assert resp.json()['ok'] == True

    @allure.story("获取课程详情")
    def test_detail(self):
        path = '/api/courses/v3/114/detail'
        resp = http.get(path)
        assert resp.status_code == 200
        assert resp.json()['ok'] == True

    @allure.story("获取菜单")
    def test_modules(self):
        path = '/api/courses/v3/114/modules/'
        resp = http.get(path)
        assert resp.status_code == 200
        assert resp.json()['ok'] == True

    @allure.story("获取大纲")
    def test_chapters(self):
        path = '/api/courses/v3/114/chapters'
        resp = http.get(path)
        assert resp.status_code == 200
        assert resp.json()['ok'] == True

    @allure.story("获取章节")
    def test_chapterDetailself(self):
        path = '/api/courses/v3/114/chapterDetail'
        resp = http.get(path)
        assert resp.status_code == 200
        assert resp.json()['ok'] == True

    @allure.story("获取小节详情")
    def test_lesson(self):
        path = '/api/learning/v3/114/lesson/ke-cheng-dao-xue/'
        resp = http.get(path)
        assert resp.status_code == 200
        assert resp.json()['ok'] == True