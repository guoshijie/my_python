# coding:utf-8

#    __author__ = 'Guo Shijie'
#    __date__ = '2016/5/26'
#    __Desc__ =  测试测试  刷新自己的博客的浏览量

import urllib2,re
import random
from bs4 import BeautifulSoup

user_agent_list = [
	    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
	    'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
	    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
	    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
	    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
	    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
	    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
	    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
	    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
	    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
	    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
	    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
]

def getHtml(url,headers):
    req = urllib2.Request(url,headers=headers)
    page = urllib2.urlopen(req)
    html = page.read()
    return html

def parse(data):
    content = BeautifulSoup(data,'lxml')
    return content

def getReadNums(data,st):
    reg = re.compile(st)
    return re.findall(reg,data)

url = 'http://blog.csdn.net/github_33644920/article/details/53485632'

def getHeaders():
	headers = {
		'referer':'http://blog.csdn.net/',
		'User-Agent':random.choice(user_agent_list)
	}
	return headers

for i in range(100):
    html = getHtml(url,getHeaders())
    content = parse(html)
    result = content.find_all('span',class_='link_view')
    print result[0].get_text()

