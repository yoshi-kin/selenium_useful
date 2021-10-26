# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
from wait_driver import WaitDriver
import time
import traceback


def test_wd():
    options = Options()
    # linux上で動かすときは次の2つも実行してください。
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    wd = WaitDriver(driver)
    try:
        wd.get("https://github.com/")
        wd.click('/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a')
        wd.set_driver(driver)
        wd.send_keys('//*[@id="login_field"]', 'kinrou2016@gmail.com')
        wd.send_keys('//*[@id="password"]', 'garoooo0')
        wd.click('//*[@id="login"]/div[4]/form/div/input[12]')
        wd.click('//*[@id="repos-container"]/form/button')
        wd.click('//*[@id="repos-container"]/ul[2]/li[5]/div/div/a')
        # wd.move_to_element('//*[@id="dashboard"]/div/div[4]/h2')
    except Exception:
        print(traceback.format_exc())
    finally:
        time.sleep(2)
        wd.quit()


def test_org():
    try:
        options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options)
        url = "https://github.com/"
        driver.get(url)
        driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a').click()
        driver.find_element_by_xpath('//*[@id="login_field"]').send_keys('kinrou2016@gmail.com')
        driver.find_element_by_xpath('//*[@id="password"]').send_keys('garoooo0')
        driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]').click()
        driver.find_element_by_xpath('//*[@id="repos-container"]/form/button').click()
        driver.find_element_by_xpath('//*[@id="repos-container"]/ul[2]/li[5]/div/div/a').click()
    except Exception:
        print(traceback.format_exc())
    finally:
        time.sleep(2)
        driver.quit()


if __name__ == '__main__':
    test_wd()
    # test_org()
