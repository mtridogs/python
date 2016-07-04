# -*- coding: cp936 -*-
#coding=utf-8
from urlparse import urlparse
import urllib2
import re
import threading
import time
import cookielib
import csv
from webspider403 import BrowserBase
phonesoftlist=[]
spider = BrowserBase()
#seed_url = "http://sj.zol.com.cn/top/"
seed_url = "http://zhushou.360.cn/list/index/cid/12"
htmls = spider.openurl(seed_url)
html = htmls.read()
#html = "class="soft-title" title=".*">(.*)</a>',html.read()) ZOL Phone
phoneofnumberlist=re.findall(r'<li>[\s\S]*<h3><a[\s\S]*>([\s\S]*)</a>[\s\S]*</h3>[\s\S]*<span>([\s\S]*)</span>[\s\S]*</li>',html)
print phoneofnumberlist[0]

'''
        for i in range(len(phoneofnumberlist)):
                phonesoftlist.append(phoneofnumberlist[i])
        nextpage=listnum+1
        temp_url=seed_url+str(nextpage)+".html"
        html = spider.openurl(temp_url)
print "Scan Over!Start Write in Excel!"
with open('PhoneSoft.csv', 'wb') as csvfile:
        for hh in range(1,len(phonesoftlist)):
                excellist=[]
                excellist.append(str(hh))
                excellist.append(phonesoftlist[hh])
                print excellist
                spamwriter = csv.writer(csvfile,dialect='excel')
                spamwriter.writerow(excellist)
'''
