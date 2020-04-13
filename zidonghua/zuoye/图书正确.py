from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome("../tool/chromedriver.exe")
try:
    driver.get("https://book.douban.com")
    driver.find_element_by_link_text('豆瓣书店').click()
    mainWindow = driver.current_window_handle
    driver.switch_to.window(mainWindow)
    while True:
        books = driver.find_elements_by_css_selector(".book-list li")
        for book in books:
            book_link = book.find_element_by_css_selector(".book-item a div")
            book_link.click()
            driver.switch_to.window(driver.window_handles[1])
            print(driver.find_element_by_css_selector('.book-breintro h3').text)
            driver.close()
            driver.switch_to.window(mainWindow)
        next_page = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.paginator > *:last-child')))
        # next_page = driver.find_element_by_css_selector('.item_con_pager .pager_container span:last-child')
        next_page_class = next_page.get_attribute('class')

        if 'current' in next_page_class:
            break
        else:
            next_page.click()
            time.sleep(3)

finally:
    time.sleep(10)
    driver.quit()