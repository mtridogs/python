# -*- coding: cp936 -*-
#coding=utf-8
from urlparse import urlparse
import urllib2
import re
import threading
import time

exitFlag = 0
threadLock = threading.Lock()
threads = []
gurllist=[]


def gethtml(url):
        print "正在读取网页："+url
        htmls=urllib2.urlopen(url)
        html=htmls.read()
        return html

    

def searchnew(url):
    coun = gurllist.count(url)
    if coun==0:
        page = gethtml(weburl)
        htmlurl = re.findall(r'[a-zA-z]+://[^\s("\s)<>]*(?!:.css|.js)',page)#网页网址
        #htmlurl = re.findall(r'[a-zA-z]+://[^\s("\s)<>]*',page)#网页网址
        getpost(url)
        gurllist.append(url)
        for index in range(len(htmlurl)):
            myth=mythread(index,htmlurl[index])
            myth.start()
        return
    else:
        return

def getpost(url):
    page = gethtml(url)
    pmet = re.findall(r'<form.*>',page)#post
    for index in range(len(pmet)):
        method=re.findall(r'method=\"(.+)\"',pmet[index])
        action=re.findall(r'action=\"(.+)\"',pmet[index])
        fp = open('myrecordweburl.txt','a')
        fp.write("上传点为："+action[0]+"上传方式为："+method[0]+"\n")
        fp.flush()
        fp.close()
    print url+"搜索完成,该页面有"+str(len(pmet))+"个上传点"
    return

class mythread (threading.Thread):
    def __init__(self,threadID,myurl):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.url = myurl
    def run(self):
        threadLock.acquire()
        searchnew(self.url)
        threadLock.release()
        return 

print 'http or https?'
ch=raw_input('1.http  2.https:')

if ch == '1':
    weburl='http://'+raw_input("please input web url:")
elif ch== '2':
    weburl='https://'+raw_input("please input web url:")
else:
    print 'ERROR!'
    
searchnew(weburl)


