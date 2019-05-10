# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Login_page(unittest.TestCase):
    def __init__(self):
        chrome_driver_location = "/home/Music/Automation/UI_Automation_env/chromedriver-Linux64" 
        #location to you chromedriver.
        self.driver = webdriver.Chrome(chrome_driver_location)
        self.driver.implicitly_wait(30)
        self.base_url = "https://automate.io"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login_testing(self):
        # Invalid password
        driver = self.driver
        driver.get(self.base_url + "/app/login")

        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("email").send_keys("testcheck@mailinator.com")
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys("1234567")
        self.driver.find_element_by_css_selector("button.btn.btn-login").click()
        self.time.sleep(5)
        self.assertEqual("Login email or password incorrect.", driver.find_element_by_xpath("//div/div").text)

    def test_login_by_invalid(self):
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("email").send_keys("testcheck@mailinato.com")
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys("12345678")
        self.driver.find_element_by_css_selector("button.btn.btn-login").click()
        self.time.sleep(3)
        self.assertEqual("Login email or password incorrect.", driver.find_element_by_xpath("//div/div").text)

    def test_login_by_invalid_2(self):
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("email").send_keys("testcheckmailinato.com")
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys("12345678")
        self.driver.find_element_by_css_selector("button.btn.btn-login").click()
        self.time.sleep(3)
        self.assertEqual("Your email seems to be invalid.", driver.find_element_by_css_selector("p.errormessage.text-danger").text)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
