from time import sleep

from lxml.etree import XPath
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from config.Browser_driver import browser_driver

def test_dws_148():
    driver = browser_driver().browser_init()
    driver.maximize_window()
    driver.get("http://novel.hctestedu.com/user/login.html")
    driver.find_element(By.ID,"txtUName").send_keys("18687180972")
    driver.find_element(By.XPATH,"//*[@id='txtPassword']").send_keys("114514")
    driver.find_element(By.CLASS_NAME,"btn_red").click()
    sleep(3)
    driver.find_element(By.LINK_TEXT, "我的书架").click()
    sleep(5)
    driver.find_element(By.LINK_TEXT, "娇女攻略").click()
    sleep(3)
    driver.find_element(By.LINK_TEXT, "点击阅读").click()
    sleep(3)
    btn=driver.find_element(By.LINK_TEXT, "已收藏").text
    assert btn == "已收藏"
    driver.quit()
