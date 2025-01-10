from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension('coordinates.crx')
options_chrome.add_argument('--no-sandbox')
options_chrome.add_argument('--headless')

def translate(words: str) -> str:
    with webdriver.Chrome(options=options_chrome) as driver:
        driver.implicitly_wait(3)
        driver.get('https://translate.yandex.ru/?source_lang=ru&target_lang=en')
        driver.find_element(By.ID, 'fakeArea').send_keys(words)
        time.sleep(1)
        res = driver.find_element(By.CSS_SELECTOR, 'p[dir="ltr"]')
        return res.text

