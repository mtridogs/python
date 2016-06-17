from urlparse import urlparse
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
def getImg(html):
    reg = 'img src=.*'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist


html = getHtml("http://www.hao123.com")

print getImg(html)


