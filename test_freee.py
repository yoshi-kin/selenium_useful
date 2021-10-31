# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
from wait_driver import WaitDriver
import time
import traceback
import datetime
import os
from dotenv import load_dotenv
load_dotenv()



def test_wd():
    freee_url = os.environ.get("FREEE_URL")
    email = os.environ.get("FREEE_EMAIL")
    password = os.environ.get("FREEE_PASSWORD")
    options = Options()
    # linux上で動かすときは次の2つも実行してください。
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1200,1500)
    wd = WaitDriver(driver)
    try:
        wd.get(freee_url)
        wd.send_keys('//*[@id="user_email"]', text=email)
        wd.send_keys('//*[@id="login-page"]/main/div/form/div/div[3]/input[1]', text=password)
        wd.click('//*[@id="login-page"]/main/div/form/div/div[5]/input')
        wd.click('/html/body/div[1]/div/div[2]/div/div/div/nav[1]/ul/li[3]/a/span')
        tbody = driver.find(tag_name='tbody')
        trs = tbody.find_elements_by_tag_name('tr')
        for tr in trs:
            tds = tr.find_elements_by_tag_name('td')
            for td in tds:
                data_date = td.get_attribute("data-date")
                if data_date == datetime.datetime.now().strftime("%Y-%m-%d"):
                    break
            else:
                continue
            break
        td.click()
        wd.click('/html/body/div[16]/div/div/div/div/div[3]/div[2]/button[1]')
    except Exception:
        print(traceback.format_exc())
    finally:
        time.sleep(5)
        driver.quit()


if __name__ == '__main__':
    test_wd()
    # test_org()
