# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://www.baidu.com")
# driver.find_element_by_id("kw").send_keys("seleinum")
# driver.implicitly_wait(3)
# driver.find_element_by_css_selector("input[id='su']").click()
# wenben=driver.find_element_by_css_selector("div[id='1'] h3 a")
# print(wenben.text)
# driver.close()


# from selenium import webdriver
# from selenium.webdriver.support.wait import  WebDriverWait
# from selenium.webdriver.support import  expected_conditions as EC
# from  selenium.webdriver.common.by import  By
# driver=webdriver.Chrome("./tool/chromedriver.exe")
# driver.get("https://www.baidu.com")
# try:
#     element=WebDriverWait(driver,3).until(
#         EC.element_to_be_clickable((By.LINK_TEXT,'新闻'))
#     # WebDriverWait(driver, 3).until(EC.number_of_windows_to_be(2))判断打开窗口是否为2
#     )
#     element.click()
#     print(driver.find_element_by_tag_name('title').get_attribute('text'))
# except:
#     print("查找出错")
# finally:
#     driver.quit()



# from selenium import webdriver
# driver=webdriver.Chrome("./tool/chromedriver.exe")
# driver.get("file:///E:/selenium/selenium_pages-master/swtich_window_sample.html")
# mainWindow=driver.current_window_handle
# driver.execute_script("""window.open("https://cn.bing.com/");""")
# driver.switch_to.window(driver.window_handles[1])
# # print(driver.find_element_by_tag_name('title').get_attribute('text'))
# driver.switch_to.window(mainWindow)
# driver.quit()

# from selenium import webdriver
# driver=webdriver.Chrome("./tool/chromedriver.exe")
# driver.get("file:///E:/selenium/selenium_pages-master/iframe_sample.html")
# driver.switch_to.frame('innerFrame')
# xdcai=driver.find_elements_by_xpath("//div[@class='plant']")
# for cai in xdcai:
#     print(cai.text)
# driver.switch_to.default_content()
# driver.close()

# from selenium import webdriver
# driver=webdriver.Chrome("./tool/chromedriver.exe")
# driver.get("https://www.baidu.com")
# driver.get("https://www.baidu.com/s?ie=UTF-8&wd=selenium")
# # driver.find_element_by_id("kw").send_keys("seleinum")
# # driver.find_element_by_id("su").click()
# driver.back()
# driver.forward()
# driver.close()

# from selenium import webdriver
# driver=webdriver.Chrome("./tool/chromedriver.exe")
# driver.get("https://www.baidu.com")
# driver.find_element_by_link_text('新闻').click()
# driver.back()
# driver.forward()
# driver.close()

# from selenium import webdriver
# import time
# def my_refresh(url,num):
#     driver=webdriver.Chrome("./tool/chromedriver.exe")
#     driver.get(url)
#     for i in range(num):
#         driver.refresh()
#         time.sleep(1)
#     else:
#         print("刷新完成")
#     driver.quit()
# my_refresh("https://www.baidu.com",5)


# from selenium import webdriver
# from time import sleep
#
# browser = webdriver.Chrome()
# browser.get("https://tieba.baidu.com/")
# sleep(2)
# # 开始控制滚动条滚动到小说指定位置
# elment = browser.find_element_by_css_selector(".title>a[title='地区']")
# browser.execute_script("arguments[0].scrollIntoView();", elment)
# browser.execute_script("var q=document.documentElement.scrollTop=0")#顶部
# browser.execute_script("var q=document.documentElement.scrollTop=100000")#底部
# sleep(5)
# browser.quit()


# from selenium import webdriver
# driver=webdriver.Chrome("./tool/chromedriver.exe")
# driver.get("file:///E:/selenium/selenium_pages-master/form_web_element.html")
# print(driver.find_element_by_css_selector("#s_radio input[checked=checked]").get_attribute('value'))
# driver.find_element_by_css_selector("#s_radio input[value='小雷老师']").click()

# from selenium import webdriver
# driver=webdriver.Chrome("./tool/chromedriver.exe")
# driver.get("file:///E:/selenium/selenium_pages-master/form_web_element.html")
# driver.find_element_by_css_selector("#s_checkbox input[value='小凯老师']").click()
# driver.find_element_by_css_selector("#s_checkbox input[value='小雷老师']").click()


# from selenium import webdriver
# driver=webdriver.Chrome("./tool/chromedriver.exe")
# driver.get("https://www.lagou.com/zhaopin/Java/?labelWords=label")
# while True:
#     jobs=driver.find_elements_by_css_selector(".item_con_list li")
#     driver.find_element_by_css_selector(".body-btn").click()
#     for job in jobs:
#         job_link=job.find_element_by_css_selector(".p_top a span")
#         job_link.click()
#         mainWindow=driver.current_window_handle
#         driver.switch_to.window(driver.window_handles[1])
#         print(driver.find_element_by_css_selector('.job-name h4').text)
#         print(driver.find_element_by_css_selector('.job-name h1').text)
#         print(driver.find_element_by_css_selector('.job_request h3 .salary').text)
#         print(driver.find_element_by_css_selector('.job_request  h3 span:nth-child(3)').text)
#         driver.close()
#         driver.switch_to.window(mainWindow)
#     if driver.find_element_by_css_selector(".pager_container a:nth-child(6)").get_attribute(
#                 'herf') != "javascript:;":
#         driver.find_element_by_css_selector(".pager_container a:nth-child(6)").click()
#     else:
#         break


# from selenium import webdriver
# driver=webdriver.Chrome("./tool/chromedriver.exe")
# try:
#     driver.get("https://book.douban.com")
#     driver.find_element_by_link_text('豆瓣书店').click()
#     mainWindow=driver.current_window_handle
#     driver.switch_to.window(mainWindow)
#     while True:
#         books=driver.find_elements_by_css_selector(".book-list li")
#         for book in books:
#             book_link=book.find_element_by_css_selector(".book-item a div")
#             book_link.click()
#             driver.switch_to.window(driver.window_handles[1])
#             print(driver.find_element_by_css_selector('.book-breintro h3').text)
#             driver.close()
#             driver.switch_to.window(mainWindow)
#         if driver.find_element_by_css_selector(".paginator a:nth-child(6)").get_attribute('class') != 'item current':
#             driver.find_element_by_css_selector(".paginator a:nth-child(6)").click()
#         else:
#             break
# finally:
#     driver.quit()
