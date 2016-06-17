from urlparse import urlparse
import urllib2

def mygethtml(url):#url must is http://+url.com
		print "downing web page now"+url
		htmls=urllib2.urlopen(url)
		html=htmls.read()
		return html