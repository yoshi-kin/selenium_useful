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

    def get(self, url):
        self.__driver.get(url)

    def quit(self, sleep=SLEEP):
        time.sleep(sleep)
        self.__driver.quit()

    def find(
                self, 
                xpath=None, 
                id=None, 
                class_name=None, 
                tag_name=None, 
                timeout=TIMEOUT
            ):
        wait = WebDriverWait(self.__driver, timeout)
        if xpath is not None:
            visbility = expected_conditions.visibility_of_element_located(
                            (By.XPATH, xpath)
                        )
        elif id is not None:
            visbility = expected_conditions.visibility_of_element_located(
                            (By.ID, id)
                        )
        elif class_name is not None:
            visbility = expected_conditions.visibility_of_element_located(
                            (By.CLASS_NAME, class_name)
                        )
        elif tag_name is not None:
            visbility = expected_conditions.visibility_of_element_located(
                            (By.TAG_NAME, tag_name)
                        )
        element = wait.until(visbility)
        return element
    
    def click(
                self, 
                xpath=None, 
                id=None, 
                class_name=None, 
                tag_name=None, 
                timeout=TIMEOUT, 
                sleep=SLEEP
            ):
        wait = WebDriverWait(self.__driver, timeout)
        if xpath is not None:
            clickable = expected_conditions.element_to_be_clickable(
                            (By.XPATH, xpath)
                        )
        elif id is not None:
            clickable = expected_conditions.element_to_be_clickable(
                            (By.ID, id)
                        )
        elif class_name is not None:
            clickable = expected_conditions.element_to_be_clickable(
                            (By.CLASS_NAME, class_name)
                        )
        elif tag_name is not None:
            clickable = expected_conditions.element_to_be_clickable(
                            (By.TAG_NAME, tag_name)
                        )
        element = wait.until(clickable)
        time.sleep(sleep)
        element.click()
        return element

    def send_keys(
                    self, 
                    xpath=None, 
                    id=None, 
                    class_name=None, 
                    tag_name=None, 
                    text='', 
                    timeout=TIMEOUT, 
                    sleep=SLEEP
                ):
        if xpath is not None:
            element = self.find(xpath=xpath, timeout=timeout)
        elif id is not None:
            element = self.find(id=id, timeout=timeout)
        elif class_name is not None:
            element = self.find(class_name=class_name, timeout=timeout)
        elif tag_name is not None:
            element = self.find(tag_name=tag_name, timeout=timeout)
        time.sleep(sleep)
        element.send_keys(text)
        return element

    def move_to_element(
                            self, 
                            xpath=None, 
                            id=None, 
                            class_name=None, 
                            tag_name=None, 
                            timeout=TIMEOUT, 
                            sleep=SLEEP
                        ):
        if xpath is not None:
            element = self.find(xpath=xpath, timeout=timeout)
        elif id is not None:
            element = self.find(id=id, timeout=timeout)
        elif class_name is not None:
            element = self.find(class_name=class_name, timeout=timeout)
        elif tag_name is not None:
            element = self.find(tag_name=tag_name, timeout=timeout)
        actions = ActionChains(self.__driver)
        actions.move_to_element(element)
        time.sleep(sleep)
        actions.perform()
        return element

    def drug_and_drop(
                        self, 
                        drag_xpath=None, 
                        drop_xpath=None, 
                        drag_id=None, 
                        drop_id=None, 
                        drag_class_name=None, 
                        drop_class_name=None, 
                        drag_tag_name=None, 
                        drop_tag_name=None, 
                        timeout=TIMEOUT, 
                        sleep=SLEEP
                    ):
        if drag_xpath is not None:
            source = self.find(xpath=drag_xpath, timeout=timeout)
        elif drag_id is not None:
            source = self.find(id=drag_id, timeout=timeout)
        elif drag_class_name is not None:
            source = self.find(class_name=drag_class_name, timeout=timeout)
        elif drag_tag_name is not None:
            source = self.find(tag_name=drag_tag_name, timeout=timeout)
        
        if drop_xpath is not None:
            target = self.find(xpath=drop_xpath, timeout=timeout)
        elif drop_id is not None:
            target = self.find(id=drop_id, timeout=timeout)
        elif drop_class_name is not None:
            target = self.find(class_name=drop_class_name, timeout=timeout)
        elif drop_tag_name is not None:
            target = self.find(tag_name=drop_tag_name, timeout=timeout)
    
        actions = ActionChains(self.__driver)
        actions.click_and_hold(source)
        actions.move_to_element(target)
        time.sleep(sleep)
        actions.perform()
        return source, target
