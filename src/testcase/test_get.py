# -*- coding: utf-8 -*-
__author__ = 'zhongyaqi'
#通过python requests访问接口的方式获取https://xueqiu.com/hq ;页面的涨跌幅榜的股票

import  requests,pytest


@pytest.mark.parametrize("size,order", [
            (10, 'desc'),(20,"asc")])
def test_ganggu(size,order):
    mypayload = {'page': '1', 'size': size,'order':order,'orderby':'percent','order_by':'percent','market':'HK','type':'hk','_':'1553416305026'}
    myheader={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
    url='https://xueqiu.com/service/v5/stock/screener/quote/list'
    res=requests.get(url,verify=False,headers=myheader,params=mypayload)
    print (res.json())
    listlenth=len(res.json().get("data").get("list"))
    assert listlenth==10 or 20




def test_shouye():
    myheader={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
    url='https://xueqiu.com/service/v5/stock/screener/quote/list?type=sha&order_by=percent&order=desc&size=10&page=1&_=1553412647861'
    res=requests.get(url,verify=False,headers=myheader)
    print(res.json())
    print('res.json--------------------')
    print(res.content)
    print('res.content--------------------')
    print(res.text)
    print('res.text--------------------')
    #<Response [403]>
