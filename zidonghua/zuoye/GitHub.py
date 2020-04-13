from selenium import webdriver
import time


driver=webdriver.Chrome("d:/webdrivers/chromedriver.exe")
driver.get("https://github.com/login")
deng_text=driver.find_element_by_xpath("//input[@id='login_field']")
pw_text=driver.find_element_by_xpath("//input[@id='password']")
deng_text.send_keys("adminbxm")
pw_text.send_keys("gbb879776609")
login=driver.find_element_by_xpath("//input[@class='btn btn-primary btn-block']")
login.click()
# cs=driver.find_element_by_xpath("//span[@class='flex-shrink-0 css-truncate css-truncate-target']")
# if cs.text=='adminbxm':
#     print("登录成功")
time.sleep(5)
xl=driver.find_elements_by_xpath("//summary[@class='Header-link']")
xl[1].click()
time.sleep(5)
dc_text=driver.find_element_by_xpath("//a[@href='/login']")
# else:
#     print("登录失败")
driver.close()