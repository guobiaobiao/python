# # 1.
# from selenium import webdriver
# driver=webdriver.Chrome("./tool/chromedriver.exe")
# driver.get("https://www.baidu.com")
# elements=driver.find_elements_by_tag_name("a")
# for element in elements:
#     print(element.text)

# # 2.
# from selenium import webdriver
# import re
# driver =webdriver.Chrome()
# driver.get("http://home.baidu.com/contact.html")
# html_source=driver.page_source
# # emails=re.findall(r'\w+@baidu.com',html_source)
# emails=re.findall(r'\w+@[a-z0-9]+\.[a-z]{2,4}',html_source)
# for email in emails:
#     print(email)
# driver.close()

# # 3.
# from selenium import webdriver
# driver=webdriver.Chrome("d:/webdrivers/chromedriver.exe")
# driver.get("http://v3.alphacoding.cn/")
# elements=driver.find_elements_by_tag_name("img")
# for element in elements:
#     print(element.text)
# if element.text.get_attribute('src')=="image/logo.svg" or "signin-page-drawing.svg":
#     print("正确")
# else:
#     print("错误")