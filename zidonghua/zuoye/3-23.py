# from selenium import webdriver
# from  selenium.webdriver.support.ui import Select
# driver=webdriver.Chrome("./tool/chromedriver.exe")
# driver.get("file:///E:/selenium/selenium_pages-master/form_web_element.html")
# select_teacher=Select(driver.find_element_by_id('ss_single'))
# assert len(select_teacher.options)==3
# driver.close()

# from selenium import webdriver
# from  selenium.webdriver.support.ui import Select
# driver=webdriver.Chrome("./tool/chromedriver.exe")
# driver.get("file:///E:/selenium/selenium_pages-master/form_web_element.html")
# select_teacher=Select(driver.find_element_by_id('ss_multi'))
# select_teacher.deselect_by_value("小凯老师")
# select_teacher.select_by_value("小雷老师")
# driver.close()

# from selenium import webdriver
# import time
# from selenium.webdriver.common.alert import Alert
# driver=webdriver.Chrome("./tool/chromedriver.exe")
# driver.get("file:///E:/selenium/selenium_pages-master/alert.html")
# time.sleep(2)
# driver.find_element_by_id('b1').click()
# driver.switch_to.alert.accept()
# driver.close()

# from selenium import webdriver
# import time
# from selenium.webdriver.common.alert import Alert
# driver=webdriver.Chrome("./tool/chromedriver.exe")
# driver.get("file:///E:/selenium/selenium_pages-master/alert.html")
# time.sleep(2)
# driver.find_element_by_id('b2').click()
# driver.switch_to.alert.accept()
# time.sleep(2)
# driver.find_element_by_id('b2').click()
# driver.switch_to.alert.dismiss()
# driver.close()

# from selenium import webdriver
# import time
# from selenium.webdriver.common.alert import Alert
# driver=webdriver.Chrome("./tool/chromedriver.exe")
# driver.get("file:///E:/selenium/selenium_pages-master/alert.html")
# time.sleep(2)
# driver.find_element_by_id('b3').click()
# print(driver.switch_to.alert.text)
# driver.switch_to.alert.send_keys('你好')
# driver.switch_to.alert.accept()
# time.sleep(2)
# driver.find_element_by_id('b3').click()
# driver.switch_to.alert.dismiss()
# driver.close()

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# driver=webdriver.Chrome("./tool/chromedriver.exe")
# driver.get("https://www.baidu.com")
# ac=ActionChains(driver)
# ac.move_to_element(driver.find_element_by_name('tj_briicon')).perform()
# driver.close()

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# driver=webdriver.Chrome("./tool/chromedriver.exe")
# driver.get("https://www.baidu.com")
# ac=ActionChains(driver)
# ac.context_click(driver.find_element_by_css_selector("img[class='index-logo-src']")).send_keys(Keys.ARROW_DOWN+Keys.ENTER).perform()
# driver.switch_to.window(driver.window_handles[1])
# assert driver.title =='今日新鲜事_百度搜索'
# driver.close()
