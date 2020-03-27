from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome("driver/chromedriver", options=options)

driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("python", Keys.RETURN)

width = driver.execute_script("return document.body.scrollWidth;")
height = driver.execute_script("return document.body.scrollHeight;")
driver.set_window_size(width, height)
driver.save_screenshot('screenshot/screenshot-full.png')

# 終了する
driver.quit()
