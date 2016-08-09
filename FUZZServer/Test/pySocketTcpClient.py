import socket  
import time
address = ('192.168.2.1',80)  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.connect(address)
var=1

import datetime
now = datetime.datetime.now()
now.strftime('%Y-%m-%d %H:%M:%S')



data = s.recv(1024)
data.strip()
print now.strftime('%Y-%m-%d %H:%M:%S'),"  Echo:  ",data
s.send('SSH-2.0-nsssh2_5.0.0021 NetSarang Computer, Inc.')




s.close()
