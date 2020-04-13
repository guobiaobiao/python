from  common.commonDate import CommonDate
from  util.httpUtil import HttpUtil
import pytest
from common.date1 import date1
from common.date2 import date2
from common.date3 import date3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 返回文件路径
LOG_DIR = BASE_DIR + "/logs/"

http=HttpUtil()
@pytest.fixture(scope='session',autouse=True)
def session_fixtrue():
    path='/api/auth/login'

    date={'loginId':CommonDate.mobile,
          'password':CommonDate.password,
          'orgId':CommonDate.orgId}
    resp=http.post(path,date)
    print("登录成功")

@pytest.fixture(scope='session',autouse=True)
def session_fixtrue1():
    path='/api/courses/v3/trends'
    resp=http.get(path)
    print("查看学习动态成功")

@pytest.fixture(scope='session',autouse=True)
def session_fixtrue2():
    path='/api/courses/v3/myCourses'
    resp=http.get(path)
    print("获取课程列表")

@pytest.fixture(scope='session',autouse=True)
def session_fixtrue3():
    path='/api/learning/v3/114/recentLesson'
    resp=http.get(path)
    print("获取最近学习小节")


@pytest.fixture(scope='session',autouse=True)
def session_fixtrue4():
    path='/api/courses/v3/114/courseRole/'
    resp=http.get(path)
    print("获取课程角色")

@pytest.fixture(scope='session',autouse=True)
def session_fixtrue5():
    path='/api/courses/v3/114/detail'
    resp=http.get(path)
    print("获取课程详情")

@pytest.fixture(scope='session',autouse=True)
def session_fixtrue6():
    path='/api/courses/v3/114/modules/'
    resp=http.get(path)
    print("获取菜单")

@pytest.fixture(scope='session',autouse=True)
def session_fixtrue7():
    path='/api/courses/v3/114/chapters'
    resp=http.get(path)
    print("获取大纲")

@pytest.fixture(scope='session',autouse=True)
def session_fixtrue8():
    path='/api/courses/v3/114/chapterDetail'
    resp=http.get(path)
    print("获取章节")

@pytest.fixture(scope='session',autouse=True)
def session_fixtrue9():
    path='/api/learning/v3/114/lesson/ke-cheng-dao-xue/'
    resp=http.get(path)
    print("获取小节详情")
    
@pytest.fixture(scope='session',autouse=True)
def session_fixtrue10():
    path='/api/record/recordStudyTime/'
    date=date1["date1"]
    resp=http.post(path,date)
    print("时间响应成功")

@pytest.fixture(scope='session',autouse=True)
def session_fixtrue11():
    path='/api/learning/v3/run'
    date=date2["date2"]
    resp=http.post(path,date)
    print("运行成功")

@pytest.fixture(scope='session',autouse=True)
def session_fixtrue12():
    path='/api/learning/v3/judge'
    date=date3["date3"]
    resp=http.post(path,date)
    print("提交成功")