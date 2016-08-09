import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')


r = requests.get('http://www.cnblogs.com/')
print r.text