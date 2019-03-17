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
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_hogwarts(self):
        driver = self.driver
        driver.get("https://testing-studio.com/")
        driver.maximize_window()
        driver.find_element_by_link_text(u"学院首页").click()
        driver.find_element_by_link_text(u"技术服务").click()
        driver.find_element_by_link_text(u"近期内推职位").click()
        driver.find_element_by_link_text(u"关于我们").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='https://testerhome.com/'])[1]/following::p[2]").click()

    def test_hogwarts_headless(self):

        headless_option=webdriver.ChromeOptions()
        headless_option.headless=True
        self.driver = webdriver.Chrome(options=headless_option)
        self.driver.get("https://testing-studio.com/")
        print(self.driver.page_source,encoding='utf-8')
        self.driver.find_elements()



    def test_mulWindows(self):
        driver=self.driver
        driver.get("https://testerhome.com/")
        ##无法通过css_selector定位到测试工程师生存指南++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # elements=driver.find_elements_by_css_selector('a[title=测试工程师生存指南]')
        # print(elements)

        # driver.find_element(By.CSS_SELECTOR,"title=测试工程师生存指南").click()
        driver.find_element(By.PARTIAL_LINK_TEXT,"测试工程师生存指南").click()
        time.sleep(5)
        assert driver.find_element(By.CSS_SELECTOR,"#前言")
        page=driver.page_source
        print(page)
        #执行完报错File-Setting-File Encoding 设置成utf-8


        ##不支持getElementById+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # js_lookfor="var q =document.getElementById('前言)"
        # driver.execute_script(js_lookfor).click()
        # driver.save_screenshot("./js_lookfor.jpg")
        # handles=driver.window_handles
        # print(handles)
        # driver.switch_to.window(handles[1])
        # print(driver.page_source)


    def test_hogwarts_runjs(self):
        driver=self.driver
        driver.get("https://testing-studio.com/")
        #将滚动条移动到页面的底部
        js_ToBottom="var q=document.documentElement.scrollTop=100000"
        driver.execute_script(js_ToBottom)
        driver.save_screenshot("./js_ToBottom.png")
        time.sleep(5)

        #将滚动条移动到页面的顶部
        js_ToTop="var q=document.documentElement.scrollTop=0"
        driver.execute_script(js_ToTop)
        driver.save_screenshot("./js_ToTop.png")
        time.sleep(5)

    def test_scrollFindelement(self):
        driver=self.driver
        driver.get("https://testing-studio.com/")
        #条件
        js_ToElement="var q=document.documentElement.scrollTop=50"
        driver.execute_script(js_ToElement)
        time.sleep(2)
        if driver.find_element(By.PARTIAL_LINK_TEXT,"了解更多内容"):
            driver.save_screenshot("./了解更多内容.png")
            time.sleep(2)
            driver.find_element(By.PARTIAL_LINK_TEXT,"了解更多内容").click()
            driver.save_screenshot("./js_ToElement1.png")
            time.sleep(2)
        else:
            driver.execute_script(js_ToElement)
            time.sleep(5)

        #循环



        #getElementById
        # js_lookfor="var q =document.getElementById('header)"
        # driver.execute_script()
        # driver.save_screenshot()

        #getElementByclassName
        # js_lookfor="var q =document.getElementByclassName('wp-block-image')"
        # driver.execute_script(js_lookfor)
        # driver.save_screenshot("./js_lookfor.png")
        # time.sleep(5)

        #若要对页面中的内嵌窗口中的滚动条进行操作，要先定位到该内嵌窗口，在进行滚动条操作
        # js="var q=document.getElementById('id').scrollTop=100000"
        # driver.execute_script(js)


        # elements = self.driver.find_element_by_xpath(position)
        # i=0
        # while i < 10:
        #     try:
        #         elements[no].click()
        #         break
        #     except Exception as e:
        #         ScripeFunc.scrollIntoWindowY(self)
        #         i = i + 1
        #         if i==10:
        #             print("no element")


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True


    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
