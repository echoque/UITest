# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Hogwarts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_hogwarts(self):
        driver = self.driver
        driver.get("https://www.douban.com//")
        driver.switch_to.window()


        # driver.find_element_by_link_text(u"学院首页").click()
        # driver.find_element_by_link_text(u"技术服务").click()
        # driver.find_element_by_link_text(u"近期内推职位").click()
        # driver.find_element_by_link_text(u"关于我们").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='https://testerhome.com/'])[1]/following::p[2]").click()
