# from selenium import webdriver
# driver= webdriver.Chrome("./tool/chromedriver.exe")
# driver.get('https://www.toutiao.com/ch/news_tech/')
# elements=driver.find_elements_by_xpath("//a[@class='link title']")
# for element in elements:
#     print(element.text)
# driver.close()


# import time
# from selenium import webdriver
# driver=webdriver.Chrome("./tool/chromedriver.exe")
# driver.get("https://www.baidu.com")
# element=driver.find_element_by_id("kw")
# element.send_keys("selenium")
# login=driver.find_element_by_xpath("//input[@id='su']")
# login.click()
# time.sleep(3)
# lianjies=driver.find_elements_by_xpath("//div[@class='result c-container ']/h3/a")
# if lianjies[0].text!="Selenium automates browsers. That's it!":
#     print("错误")
# for lianjie in lianjies:
#     print(lianjie.text)
# driver.close()



# from selenium import webdriver
# driver=webdriver.Chrome("./tool/chromedriver.exe")
# driver.get("https://github.com/login")
# element=driver.find_element_by_id("login_field")
# element.send_keys("adminbxm")
# element=driver.find_element_by_id("password")
# element.send_keys("gbb879776609")
# login=driver.find_element_by_xpath("//input[@name='commit']")
# login.click()
# if driver.find_element_by_xpath("//div/a/strong[@class='css-truncate-target']/font").get_attribute('text')!='adminbxm':
#     print("登录错误")
# # user=driver.find_element_by_xpath("//input[@name='login']")
# # pwd=driver.find_element_by_xpath("password")
# # if user.text=="adminbxm" and pwd.text=="gbb879776609":
# #     print("正确")
# # else:
# #     print("错误")


# from selenium import  webdriver
# import time
# driver=webdriver.Chrome("./tool/chromedriver.exe")
# driver.get("http://v3.alphacoding.cn/login")
# print(driver.find_elements_by_xpath("//div/a/img").get_attribute("src"))
# driver.find_element_by_id("input-1128").send_keys("123")
# driver.find_element_by_id("input-1129").send_keys("123")
# school=driver.find_elements_by_xpath("//div[@class='v-list-item v-list-item--link theme--light']")
# if len(school)== 30:
#     print("下拉列表真确")
# driver.find_elements_by_class_name("v-btn__content")