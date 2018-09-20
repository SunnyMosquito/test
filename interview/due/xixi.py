#coding=utf-8
#TCP服务器端程序
import socket
import time
import threading



def tcplink(sock,addr):
    print("accept new connection from %s:%s..." % addr)
    sock.send("Welcom!".encode())
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if data=='exit' or not data:
            break
        sock.send("hello: ".encode()+data)
    sock.close()
    print("Connection from %s:%s closed." % addr)
    
    
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # 创建一个基于ipv4 的TCP协议的socket

s.bind(('127.0.0.1',8828))  #监听端口

s.listen(5)
print("Waiting for connection......")

while True:
    sock,addr=s.accept()
    t=threading.Thread(target=tcplink,args=(sock, addr))
    t.start()