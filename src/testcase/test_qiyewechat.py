# -*- coding: utf-8 -*-

import pytest,requests


def test_getaccess_token():
    payload={'corpid':'wwfe4174faec32f8b3','corpsecret':'7VOw2P-AWzFddKCD__Ss9c4Uwl1YZwUcVWYgBPUItgI'}
    url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    res=requests.get(url,params=payload)
    # print(res.status_code)
    # print(res.url)
    return (res.json().get('access_token'))


def testpost_message():
    access_token=test_getaccess_token()
    url='https://qyapi.weixin.qq.com/cgi-bin/message/send'
    payload={
    'access_token':access_token}
    myheader={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
    # print(payload)
    #post请求，请求参数和请求body如何传入，放入data？？
    res=requests.post(url,data=payload,verify=False,headers=myheader)
    print(res.url)
    print(res.status_code)
    print(res.json())

def test_post_url():
    access_token=test_getaccess_token()
    mypayload={
    'access_token':access_token}
    # mypayload = {'ck': '', 'name': 'xxxxxxxx','password':'xxxxxx','remember':False,'ticket':''}
    myheader={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
    url='https://qyapi.weixin.qq.com/cgi-bin/message/send'
    #与get方法不同，post方法传入参数时key为'data',而get方法为'params'
    res=requests.post(url,verify=False,headers=myheader,data=mypayload)
    print(res.url)
    #post方法执行res.url不会拼接参数
    ###_______________________________________________
    print(res.json())
    # print (res.json().get('description'))
    # assert res.json().get('description')=='处理成功'





