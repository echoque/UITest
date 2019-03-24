# -*- coding: utf-8 -*-
__author__ = 'zhongyaqi'
#通过python requests访问接口的方式获取https://xueqiu.com/hq ;页面的涨跌幅榜的股票

import  requests,pytest

#
# @pytest.mark.parametrize("size,order", [
#             (10, 'desc'),(20,"asc")])
def test_ganggu():

    mypayload = {'ck': '', 'name': '18500910544','password':'Echoque0612','remember':False,'ticket':''}
    myheader={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
    url='https://accounts.douban.com/j/mobile/login/basic'
    res=requests.post(url,verify=False,headers=myheader,data=mypayload)
    print (res.json())
    print ('+++++++++++++++++++++++++++++++')
    print (res.json().get('description'))
    print ('+++++++++++++++++++++++++++++++')

    assert res.json().get('description')=='处理成功'
