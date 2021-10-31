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


url = os.environ.get("MATUYA_URL")
email = os.environ.get("MATUYA_EMAIL")
password = os.environ.get("MATUYA_PASSWORD")
store = os.environ.get("STORE")

def test_wd():
    options = Options()
    # linux上で動かすときは次の2つも実行してください。
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    try:
        wd = WaitDriver(driver)
        
        # urlにアクセス
        wd.get(url)
        
        # 「ログイン」をクリック
        wd.click('//*[@id="headerGlobal"]/ul/li[2]/a')
        
        # メールアドレス入力
        wd.send_keys('//*[@id="UserMail"]', text=email)
        
        # パスワード入力
        wd.send_keys('//*[@id="UserPassword"]', text=password)
        
        # 「ログイン」をクリック
        wd.click('//*[@id="submit_button"]')
        
        # 「店舗名」を入力
        wd.send_keys('//*[@id="ShopKeywords"]', text=store)
        
        # 「検索」をクリック
        wd.click('//*[@id="ShopIndexForm"]/div/dl/dd/input[2]')
        
        # トップに表示された店舗をクリック
        wd.click('//*[@id="main"]/section/div[2]/a')

        # 日付を選択
        current_day = wd.click('//*[@id="time_regular"]')
        optional_day = current_day.find_elements_by_tag_name('option')
        days = [day.text for day in optional_day]
        day_index = input(f'注文日を{days}の中からお選びください。インデックスで回答お願いします。')
        optional_day[int(day_index)].click()
        print(optional_day[int(day_index)].text)
        
        # 時間を選択
        current_hour = wd.click('//*[@id="time01_regular"]')
        optional_hour = current_hour.find_elements_by_tag_name('option')
        hours = [hour.text for hour in optional_hour]
        hour_index = input(f'注文時間を{hours}の中からお選びください。インデックスで回答お願いします。')
        optional_hour[int(hour_index)].click()
        print(f'{optional_hour[int(hour_index)].text}時')
        
        # 分を選択
        current_minute = wd.click('//*[@id="time02_regular"]')
        optional_minute = current_minute.find_elements_by_tag_name('option')
        minutes = [minute.text for minute in optional_minute]
        minute_index = input(f'注文分を{minutes}の中からお選びください。インデックスで回答お願いします。')
        optional_minute[int(minute_index)].click()
        print(f'{optional_minute[int(minute_index)].text}分')
        
        # 「メニューを選択」をクリック
        wd.click('//*[@id="main"]/section/ul[1]/li/a')
        category = wd.find('//*[@id="main"]/section/div/div[1]/div')
        slides = category.find_elements_by_class_name('swiper-slide')
        print(len(slides))

    except Exception:
        print(traceback.format_exc())
    finally:
        wd.quit()



if __name__ == '__main__':
    test_wd()