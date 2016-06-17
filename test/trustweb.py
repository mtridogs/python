# -*- coding: cp936 -*-
#coding=utf-8
from urlparse import urlparse
import urllib2
import re
import threading
import time

def gethtml(url):
        print "正在读取网页："+url
        htmls=urllib2.urlopen(url)
        html=htmls.read()
        return html

web = gethtml("http://www.cnblogs.com/fnng/p/3576154.html")
print web
