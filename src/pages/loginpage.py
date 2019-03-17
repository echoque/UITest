__author__ = 'zhongyaqi'

from .basepage import BasePageObject
from selenium.webdriver.common.by import By

class LoginPageObject(BasePageObject):

    '''
   变量声明，注意私有变量
    首先点击登录之前需要切换frame，故需要定义frame变量
    然后切换tab至密码登录,故需要定义一个密码登录变量
    最后分析页面有三个元素，账号输入框、密码输入框、登录按钮，故需要定义定义三个变量
    '''

    _switch_tab=(By.ID,)


    '''
    封装方法，注意私有方法
    需要理清登录的具体过程
    1、切换tab至密码登录
    2、切换frame
    3、输入账号、密码
    4、点击登录

    '''

    def __init__(self):
        pass

    def _switch_tab(self,element):
        pass

    def _switch_frame(self):
        pass



