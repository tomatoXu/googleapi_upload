import sys
from pprint import pprint
import base64
import gzip
import pprint
import StringIO
import requests

from google.protobuf import descriptor
from google.protobuf.internal.containers import RepeatedCompositeFieldContainer
from google.protobuf import text_format
from google.protobuf.message import Message, DecodeError

import googleplay_pb2

package_name = sys.argv[1]

'''============================================
	get the GALX of google.com
============================================'''

s = requests.session()
r = s.get("https://accounts.google.com")
#print (s.cookies['GALX'])

'''============================================
		login in 
==========================================='''

data = {
	"GALX":s.cookies['GALX'],
	"continue":"https://play.google.com/store",
	"followup":"https://play.google.com/store",
	"service":"googleplay",
	"pstMsg":"1",
	"dnConn":"",
	"checkConnection":"youtube:359:1",
	"checkedDomains":"youtube",
	"Email":"tomatoXu94@gmail.com", 
	"Passwd":"wc3leswciest",
}
headers = {    	
	"Host":"accounts.google.com",
	"User-Agent": "Mozilla/5.0(X11; Ubuntu; Linux x86_64; rv:31.0)Gecko/20100101 Firefox/31.0",
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
	"Accept-Encoding":"gzip,deflate",
	"Referer":"https://accounts.google.com/ServiceLogin?service=googleplay&passive=1209600&continue=https://play.google.com/store&followup=https://play.google.com/store",
	"Connection": "keep-alive",
          }
res = s.post('https://accounts.google.com/ServiceLoginAuth',data=data,headers=headers,cookies=r.cookies)
#print (res.cookies)

'''============================================
		check
==========================================='''

check_headers = {
        "Host":"accounts.google.com",
        "User-Agent": "Mozilla/5.0(X11; Ubuntu; Linux x86_64; rv:31.0)Gecko/20100101 Firefox/31.0",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
        "Accept-Encoding":"gzip,deflate",
        "Connection": "keep-alive",
	"Cache-Control":"max-age=0"
}

url = "https://play.google.com/store/apps/details?id=%s" % package_name
upload_header = {
        "Host":"play.google.com",
        "User-Agent": "Mozilla/5.0(X11; Ubuntu; Linux x86_64; rv:31.0)Gecko/20100101 Firefox/31.0",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
        "Accept-Encoding":"gzip,deflate",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Connection": "keep-alive",
	"Referer":url,
        "Pragma":"no-cache",
        "Cache-Control":"no-cache"
}

try:
	check = s.get('https://play.google.com',headers=upload_header,cookies=res.cookies)
	check1 = s.get('https://play.google.com/apps',headers=upload_header,cookies=check.cookies)
	#print (check1.content)
	print 'login success'
except:
	print 'login error'

'''===========================================
	upload install info
==========================================='''

upload_data1 = {
	"authuser":"0",
	"id":package_name,
	"device":"g72fbd7c23ce93b82",
	"xhr":"1",
	"token":"H9W6ryl8x2Dwxwo_ltTgkZsePXg:1444806795874"
}

upload_data2 = {
        "authuser":"0",
        "ids":package_name,
        "device":"g72fbd7c23ce93b82",
        "xhr":"1",
        "token":"H9W6ryl8x2Dwxwo_ltTgkZsePXg:1444806795874"
}

upload_cookies = {
	"APISID":"wYCG8tWzTXhR5wph/A2EAqLnVMI5LemzDU"
}

try:
	up_res = s.post('https://play.google.com/store/install?authuser=0',data=upload_data1,headers=upload_header,cookies = res.cookies)
	up_res = s.post('https://play.google.com/store/install?authuser=0',data=upload_data2,headers=upload_header,cookies = res.cookies)
	#print (up_res.cookies)
	play_res = s.get('https://play.google.com',headers=upload_header)
	#print (play_res.cookies)
	print 'Done!'
except:
	print 'ERROR!'

