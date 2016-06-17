import hashlib
import urllib2
import urllib
import cookielib 
import re
from getpage import *
url = 'http://ctf4.shiyanbar.com/ppc/sd.php'


cookie = cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open(url)

for item in cookie:
	print 'Name = '+item.name
	print 'Value = '+item.value



pattern_html = re.compile(r'red">(.*)</div>')  
re_html=pattern_html.findall(response.read())
mdshas=re_html[0]
print mdshas

index=0
for i in range(0,100000):
	m2 = hashlib.md5()
	m2.update(str(i))  
	MD5=m2.hexdigest()
	sha1andmd5=hashlib.sha1(MD5).hexdigest();
	if sha1andmd5==mdshas:
		print i
		index=i
		break
data = {}
data['inputNumber'] = i
post_data = urllib.urlencode(data)
req = opener.open(url,post_data)
content = req.read()
print content