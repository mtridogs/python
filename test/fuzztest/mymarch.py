# -*- coding: cp936 -*-
#coding=utf-8
import re
class mymarch:
	zstr = "t" #String for regular biaodashineirongla
	tstr = "t" #String for bei regular:)
	def mars(self):
		self.zstr = str(self.zstr)
		self.zstr.replace("\\","\\\\")
		print self.zstr
		matchObj = re.match(self.zstr,self.tstr,re.M|re.I)
		
		return 0
