#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017年5月25日

@author: liuzhe
'''
from ftplib import FTP

timeout = 30
port = 21

serverip = '10.12.12.102'
username = 'miscfile'
password = 'miscfile'


ftp = FTP()

ftp.connect(serverip, port, timeout)
ftp.login(username, password)
#print ftp.welcome
ftp.cwd('/liuzhe') #chang work directory
#ftp.rename('test.txt', 'text.py')
print ftp.pwd()
#ftp.storbinary('STOR '+'sp.sql', open('D:\sp.sql')) #上传 cmd file  这个file只要是file-like，并不一要求必须是文件
for f in ftp.nlst(): #获取当前文件列表
    print f
#ftp.retrbinary('RETR '+'sp.sql',open('D:\spp.sql','wb').write)  #第一个参数cmd  第二个为一个回调函数
#ftp.retrbinary(cmd, callback, blocksize, rest) 

#ftp.delete(filename)
print ftp.retrlines('LIST') ##获取目录文件详细信息
ftp.quit()
