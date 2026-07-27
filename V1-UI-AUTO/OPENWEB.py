from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.baidu.com")
driver.find_element(By.ID,"chat-textarea").send_keys("华测教育")
driver.find_element(By.ID,"chat-submit-button").click()
sleep(10)