# coding:utf-8
import os
import sys
import time
import urllib2

def user():
	global username
	global password
	if os.path.isfile('user.txt')==False:
		username=raw_input('Please input username:\n')
		password=raw_input('Please input password:\n')
		with open('user.txt','w+') as f:
			f.write('%s\n%s'%(username,password))
	else:
		with open('user.txt','r') as f1:
			username=f1.readline().strip()
			password=f1.readline()

def Login():
	#ip='http://192.168.168.168/0.htm'
	ip='10.10.244.11'
	#print (username,password)
	data='DDDDD=%s&upass=%s&0MKKey=123456&v6ip='%(username,password)
	'''header={
		'POST':'/0.htm HTTP/1.1',
		'Host':'192.168.168.168',
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:52.0) Gecko/20100101 Firefox/52.0',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
		'Referer':'http://192.168.168.168/0.htm',
		'Cookie':'myusername=; username=; smartdot=',
		'Connection':'close',
		'Upgrade-Insecure-Requests':'1',
		'Content-Type':'application/x-www-form-urlencoded',
		'Content-Length':'42'
		}'''
	try:
		res=urllib2.Request(url=ip,data=data)
		urllib2.urlopen(res)
	except Exception:
		time.sleep(1)
		main()


def ping():
	html='www.baidu.com'
	try:
		ping=os.system('ping -c 1 %s'%html)
	except Exception:
		time.sleep(1)
		main()
	if ping:
		print ('失败！')
		Login()
	else :
		print ('成功！')
	time.sleep(1)
	

def main():
	ping()

if __name__ =="__main__":
	user()
	Login()
	while True:
		main()
