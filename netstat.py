# -*-coding:utf-8 -*-
import os
import time

net=os.popen('netstat -an').read()  #获取网络连接信息

a=time.time()+46800            #计算时间并调整时差

ThisTime=time.localtime(a)

time=time.strftime('%Y-%m-%d %H:%M:%S',ThisTime)   #格式化时间time.localtime(time.time())

with open('sslog.txt','a') as f:   #把当前时间写入日志文件

	f.write("\n\n"+time+"\n\n")

with open('sslog.txt','a') as f:   #写入网络连接信息关闭日志文件
	f.write(net)
