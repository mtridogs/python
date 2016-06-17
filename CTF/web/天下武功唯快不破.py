# coding=gbk
import hashlib
import urllib2
import urllib
import cookielib 
import re
import time
import base64
url = 'http://ctf4.shiyanbar.com/web/10.php'


cookie = cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)
response = opener.open(url)
responseinfo = response.info();
baseinfo = responseinfo["FLAG"]
info = base64.b64decode(baseinfo)
pattern_html = re.compile(r'P0ST_THIS_T0_CH4NGE_FL4G:(.*)')
re_html=pattern_html.findall(info)
httpheaderflag=re_html[0]

data = {}
data["key"] = httpheaderflag
post_data = urllib.urlencode(data)
req = opener.open(url,post_data)
content = req.read()
print content
