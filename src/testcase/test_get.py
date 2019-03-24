# -*- coding: utf-8 -*-
#实现将雪球网页的港股列表页排序并返回对应数量的股票，降序时返回十只股票，升序时返回20只股票，并做校验

import  requests,pytest

@pytest.mark.parametrize("size,order", [
            (10, 'desc'),(20,"asc")])
def test_ganggu_order(size,order):
    mypayload = {'page': '1', 'size': size,'order':order,'orderby':'percent','order_by':'percent','market':'HK','type':'hk','_':'1553416305026'}
    myheader={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
    url='https://xueqiu.com/service/v5/stock/screener/quote/list'
    res=requests.get(url,verify=False,headers=myheader,params=mypayload)
    print (res.json())
    listlenth=len(res.json().get("data").get("list"))
    assert listlenth==size

def test_xueqiushouye():
    myheader={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
    #如果本地调试，需要通过抓包工具查看接口的请求和响应数据，可以传入proxies
    ## 注：端口号与抓包工具设置的端口号保持一致。本地charles端口号为8889
    myproxy={
        'http':'127.0.0.1:8889',
        'https':'127.0.0.1:8889'

    }
    url='https://xueqiu.com/service/v5/stock/screener/quote/list?type=sha&order_by=percent&order=desc&size=10&page=1&_=1553412647861'
    res=requests.get(url,verify=False,headers=myheader,proxies=myproxy)
    print(res.json())
    print('res.json--------------------')
    print(res.content)
    print('res.content--------------------')
    print(res.text)
    print('res.text--------------------')
