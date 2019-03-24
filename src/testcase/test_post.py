# -*- coding: utf-8 -*-
#登录豆瓣网页并校验登录成功

import  requests,pytest

def test_doubanlogin():
    mypayload = {'ck': '', 'name': 'xxxxxxxx','password':'xxxxxx','remember':False,'ticket':''}
    myheader={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
    url='https://accounts.douban.com/j/mobile/login/basic'
    #与get方法不同，post方法传入参数时key为'data',而get方法为'params'
    res=requests.post(url,verify=False,headers=myheader,data=mypayload)
    print (res.json().get('description'))
    assert res.json().get('description')=='处理成功'
