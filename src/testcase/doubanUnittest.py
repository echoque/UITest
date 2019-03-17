# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,pytest

class Hogwarts(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_douban_multiple_frame(self):
        driver = self.driver
        driver.get("https://www.douban.com/")
        frame=driver.find_element_by_tag_name('iframe')
        driver.switch_to.frame(frame)
        driver.find_element_by_class_name('account-form-link').click()

    def test_douban_multiple_windows(self):
        driver = self.driver
        driver.get("https://testing-studio.com/")
        frame=driver.find_element_by_tag_name('iframe')
        driver.switch_to.frame(frame)
        driver.find_element_by_class_name('account-form-link').click()

    def test_login(self):
        driver=self.driver
        driver.get('https://www.douban.com/')
        time.sleep(5)
        #获取并切换frame
        frame=driver.find_element_by_tag_name('iframe')
        driver.switch_to.frame(frame)
        driver.find_element(By.CLASS_NAME,'account-tab-account').click()

        #输入账号密码
        print("输入账号密码")
        #通过默认方式定位
        driver.find_element(value="username").send_keys("18500910544")
        driver.find_element(value="password").send_keys("Echoque0612")
        #通过id定位
        # driver.find_element(By.ID,'username').send_keys('18500910544')
        # driver.find_element(By.ID,'password').send_keys('Echoque0612')
        #通过css定位
        # driver.find_element(By.CSS_SELECTOR,'input[placeholder="手机号 / 邮箱"]').send_keys('18500910544')
        # driver.find_element(By.CSS_SELECTOR,'input[placeholder="密码"]').send_keys('Echoque0612')

        #点击登录豆瓣
        print("点击登录豆瓣")
        element=driver.find_element_by_link_text('登录豆瓣')
        ##高高亮显示定位的元素
        driver.execute_script("arguments[0].style.background = 'rgb(138,43,226 )';", element)
        element.click()

        #登录成功断言
        assert driver.find_element_by_link_text('我的豆瓣')


        #pytes-assume————————————————————————————————————————————
        # pytest.assume(driver.find_element_by_link_text('ssss'))
        # pytest.assume(driver.find_element_by_link_text('我的豆瓣'))

        ##需要将username和password数据分离
        # assert driver.find_element(By.CSS_SELECTOR,'a[span="echoque的帐号"]') 定位有误

