from time import sleep

from lxml.etree import XPath
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from config.Browser_driver import browser_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def test_dws_148():
    driver = browser_driver().browser_init()
    driver.maximize_window()
    driver.get("https://layui.dev/docs/2/laydate/#demo-type")
    wait = WebDriverWait(driver, 10)
    locator=(By.XPATH,'//*[@id="ID-laydate-type-year"]')
    wait.until(ec.element_to_be_clickable(locator)).send_keys("2022")
    driver.find_element(By.ID,'ID-laydate-type-time').click()



    sleep(100)