# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
from wait_driver import WaitDriver
import time
import traceback
import os
from dotenv import load_dotenv
load_dotenv()


url = os.environ.get("GITHUB_URL")
email = os.environ.get("GITHUB_EMAIL")
password = os.environ.get("GITHUB_PASSWORD")


def test_wd():
    
    options = Options()
    # linux上で動かすときは次の2つも実行してください。
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    wd = WaitDriver(driver)
    try:
        wd.get(url)
        wd.click('/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a')
        wd.set_driver(driver)
        wd.send_keys('//*[@id="login_field"]', text=email)
        wd.send_keys('//*[@id="password"]', text=password)
        wd.click('//*[@id="login"]/div[4]/form/div/input[12]')
        wd.click('//*[@id="repos-container"]/form/button')
        wd.click('//*[@id="repos-container"]/ul[2]/li[5]/div/div/a')
        # wd.move_to_element('//*[@id="dashboard"]/div/div[4]/h2')
    except Exception:
        print(traceback.format_exc())
    finally:
        time.sleep(2)
        wd.quit()


if __name__ == '__main__':
    test_wd()
