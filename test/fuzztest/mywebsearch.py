# -*- coding: cp936 -*-
#coding=utf-8
from urlparse import urlparse
import urllib2
import urllib
import re
import threading
import time

class mywebsearch:
	weburl = ""
	webhtmlT = ""
	webposturl = ""
	webposthtmlr=""

	def __init__(self):
		self.weburl="https://www.zhihu.com/"

	def getwebhtml(self): #返回网页文本
		print "START SCAN WEB HTML:"+self.weburl
		htmls=urllib2.urlopen(self.weburl)
		htmlT=htmls.read()
		self.webhtmlT=htmlT

	def getweburl(self):
		return self.weburl

	def gethtml(self):
		return self.webhtmlT

	def setweburl(self,weburl):
		self.weburl = weburl

	def webpost(self,mapsstr):  #模拟post提交，参数是map
		data = urllib.urlencode(mapsstr)
		req = urllib2.Request(self.webposturl,data)
		response = urllib2.urlopen(req)
		self.webposthtmlr = response.read()

