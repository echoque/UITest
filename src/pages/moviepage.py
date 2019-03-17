#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'zhongyaqi'
from selenium.webdriver.common.by import By
from .basepage import BasePageObject

class MoviePageObject(BasePageObject):

    #使用私有变量，其他模块无法查看
    _movie_query=(By.ID,'inp-query')
    _search_click=(By.CLASS_NAME,'inp-btn')


    def __init__(self):
        pass

    def locate_moive_query(self):
        pass

    def input_movie_query(self):
        pass