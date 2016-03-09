import os
import time

net=os.popen('netstat -an').read()

time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

with open('sslog.txt','a') as f:

	f.write(time+"\n\n\n")


with open('sslog.txt','a') as f:
	f.write(net)
