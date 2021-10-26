from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class WaitDriver:
    TIMEOUT = 20
    SLEEP = 1

    def __init__(self, driver):
        if not isinstance(driver, webdriver.Chrome):
            raise("Invalid driver type, expected for Chrome")
        self.__driver = driver

    def get_driver(self):
        return self.__driver

    def set_driver(self, driver):
        if not isinstance(driver, webdriver.Chrome):
            raise("Invalid driver type, expected for Chrome")
        self.__driver = driver

    def get(self, url):
        self.__driver.get(url)

    def quit(self):
        self.__driver.quit()

    def find(self, xpath, timeout=TIMEOUT):
        wait = WebDriverWait(self.__driver, timeout)
        element = wait.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, xpath)
            )
        )
        return element

    def send_keys(self, xpath, text, timeout=TIMEOUT, sleep=SLEEP):
        element = self.find(xpath, timeout)
        time.sleep(sleep)
        element.send_keys(text)
        return element

    def click(self, xpath, timeout=TIMEOUT, sleep=SLEEP):
        wait = WebDriverWait(self.__driver, timeout)
        element = wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, xpath)
            )
        )
        time.sleep(sleep)
        element.click()
        return element

    def move_to_element(self, xpath, timeout=TIMEOUT, sleep=SLEEP):
        element = self.find(xpath, timeout)
        actions = ActionChains(self.__driver)
        actions.move_to_element(element)
        time.sleep(sleep)
        actions.perform()
        return element

    def drug_and_drop(self, draggable_xpath, droppable_xpath, timeout=TIMEOUT, sleep=SLEEP):
        source = self.find(draggable_xpath, timeout)
        target = self.find(droppable_xpath, timeout)
        actions = ActionChains(self.__driver)
        actions.click_and_hold(source)
        actions.move_to_element(target)
        time.sleep(sleep)
        actions.perform()
        return source, target
