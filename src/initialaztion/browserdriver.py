#! /usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver

import unittest, time, re,pytest

class Hogwarts(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
