import socket
import sys

sock = socket.create_connection(('192.168.1.1',80))


try:
    me=10
    while me>0:
               data = sock.recv(16)
               me=me-1
               print data
finally:
        sock.close()
raw_input()
    
