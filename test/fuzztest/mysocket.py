# -*- coding: cp936 -*-
#coding=utf-8
import socket

class  mysock:
	host = ""
	port = ""
	recTbuff = ""
	addr = (host,port)
	

	def udpsendT(self,strsend):
		udps = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		udps.sendto(strsend,(self.host,self.port))


	def tcpsendT(self,strsend):
		tcps = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		tcps.connect(self.addr)
		while True:
			if not strsend.strip():
				break
			tcps.send(data.encode('utf8'))
			self.recTbuff = tcps.recv(1024)
			if not self.recTbuff.strip():
				break


