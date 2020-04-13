import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options

# 项目目录配置
BASE_DIR=os.path.dirname(os.path.abspath(__file__))#返回文件路径
REPORT_DIR=BASE_DIR+"/report/"
IMG_DIR=BASE_DIR+"/screenshot/"
LOG_DIR=BASE_DIR+"/logs/"
driver=None

# 配置浏览器驱动类型
driver_type="chrome"

# 配置运行URL
url="https://www.baidu.com"

# 当达到最大失败，停止执行
max_fail="5"

# 运行测试用例的目录或文件
cases_path="./testcases/"

# 定义基本测试环境
@pytest.fixture(scope='function')
def base_url():
    global url
    return url

# 启动浏览器
@pytest.fixture(scope='session',autouse=True)
def browser():
    # 全局定义浏览器驱动
    global driver
    global  driver_type

    if driver_type=="chrome":
        # 本地chrome浏览器
        driver=webdriver.Chrome()
        driver.maximize_window()

    elif driver_type =="firefox":
        # 本地firefox浏览器
        driver = webdriver.Firefox()
        driver.maximize_window()

    elif driver_type=="chrome-headless":
        # chrome headless模式
        chrome_options=CH_Options()
        chrome_options.add_argument("--headless")# 浏览器不提供可视化页面
        chrome_options.add_argument("--disable-gpu") # 禁用GPU加速
        chrome_options.add_argument("--start-maximized")#窗口最大化
        driver=webdriver.Chrome(options=chrome_options)

    elif driver_type=="firefox-headless":
        # firefox headless模式
        firefox_options=FF_Options()
        firefox_options.headless=True
        driver=webdriver.Firefox(options= firefox_options)

    else:
        raise NameError("driver驱动类型定义错误！")

    return driver

# 关闭浏览器
@pytest.fixture(scope='session',autouse=True)
def browser_close():
    yield driver
    driver.quit()
    print("test end!")