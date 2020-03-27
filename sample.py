from selenium import webdriver
import time

# driverの取得
driver = webdriver.Chrome("driver/chromedriver")
# ページの表示
driver.get("http://google.com")

# 検索してみる
elem_search_word = driver.find_element_by_name("q")
elem_search_word.send_keys("selenium")
elem_search_word.submit()

# スクショとってみる
driver.save_screenshot('screenshot/search_results.png')

# 少し待機
time.sleep(10)

# 終了する
driver.quit()
