#!/usr/bin/env python
#-*-coding:utf-8-*-
from email.mime.text import MIMEText
from email.header import Header
import smtplib
#构建邮件主体
msg['From']=Header("aa")
msg['To'] = Header("bb")
msg['Subject'] = "sub"
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# 输入Email地址和口令:
from_addr = ''
username=''
password = ""
# 输入SMTP服务器地址:
smtp_server = ''
# 输入收件人地址:
to_addr = ''

#msg可以定制更多内容
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.login(username, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
