import socket  
import time
address = ('192.168.2.1',119)  
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
s.connect(address)
var=1
while var==1:
	#data = s.recv(1024)
	#print 'the data received is',data
	s.send('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
	time.sleep(0.5)
s.close()