# coding=gbk
import hashlib
import urllib2
import urllib
import cookielib 
import re
import time
url = 'http://ctf10.shiyanbar.com:8888/date.php'


cookie = cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open(url)



pattern_html = re.compile(r'(\d*)</body>')  
re_html=pattern_html.findall(response.read())
mdshas=re_html[0]

servertime = float(mdshas)+4

data = {}
data["快点输，要不没时间了"] = servertime
post_data = urllib.urlencode(data)
req = opener.open(url,post_data)
content = req.read()
print content
