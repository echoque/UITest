#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'zhongyaqi'

'''
basepage页面设计

'''

class BasePageObject:
    def __init__(self):
        self.driver=''
        pass

    def extend_find_element(self):
        pass

    def switch_frame_by_element(self,elment):
        pass

    def get_element_text(self,element):
        return element.text

    def get_bable_content(self,table_name):
        pass

    def set_value(self,element,value):
        element.clear()
        element.click()
        element.sendkeys(value)




