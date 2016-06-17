from mysocket import *
from mywebsearch import *
from mymarch import *
import re
import time

print "***************WELCOME KFZ WEB SCANNER****************************"
print "***************TianJin University of Technology*********************"
print "***************Information Security Professional********************"
print "***************12*************2*********346*************************"
print "***************START 2016/2/1***************************************"
#MY INFORMATION******************************************************** 
#bi zhuang wan le yi xia shi code

print 'THIS WEB IS HTTP or HTTPS?'
ch=raw_input('1.HTTP  2.HTTPS:')
weburl=""
if ch == '1':
    weburl='http://'+raw_input("PLEASE INPUT WEB URL:")
elif ch== '2':
    weburl='https://'+raw_input("PLEASE INPUT WEB URL:")
else:
    print 'ERROR!'

#************************************************************************
#weburl = "https://www.zhihu.com/"
myweb = mywebsearch()#my web searcher
myre = mymarch()
postmap=dict()
postmup=dict()
#march form for next
#*************************************************************************
myweb.weburl = weburl
myweb.getwebhtml()
pages01=myweb.gethtml()
mform = re.findall(r'<form [\s\S]*</form>',pages01)#find form
direct = dict()
dirformn = dict()
for index in range(len(mform)):#every from start look
	maction = re.findall(r'action="[\S]*"\s',mform[index])
	minputtext = re.findall(r'<input\s[\S]*\stype="text"',mform[index])
	minputpassword=re.findall(r'<input\s[\S]*\stype="password"',mform[index])
	inputsum=re.findall(r'<input\s.*name=.*>',mform[index])
	TSlist=[]
	for ins in range(len(inputsum)):
		TSlist.append(str(inputsum[ins]))
	numlist=[str(len(mform)),str(maction),str(len(minputtext)),str(len(minputpassword)),str(len(inputsum))]
	direct[index]=numlist
	dirformn[index]=TSlist
#find end
#start print
#print minputtext
print "FORM SUM:"+str(len(mform))
print "********************************************************"
for index in range(len(mform)):
	print "**********************************"
	print "FORM",str(index+1),"IMFORMATION:"
	listT=direct[index]
	print "ACTION FOR:",listT[1]
	print "INPUTTEXT NUM",listT[2]
	print "INPUT PASSWORD NUM:",listT[3]
	print "INPUT UNKONW OR OTHER:",str(int(listT[4])-int(listT[3])-int(listT[2]))
	print "INPUT SUM :",listT[4]
	print "**********************************"
print "************INFORMATION  END*****************************"
#information end
#start fuck
#huo xu wo gai shi yong yi xie class
#*******************************************URL CREAT************
num=raw_input('PLEASE ENTER FORM NUM(0~n)')
#num=0
formlist = direct[int(num)]
inputlist = dirformn[int(num)]
print "CREATE URL....."
chunaction = re.findall(r'(?<=\").*?(?=\")',formlist[1])#pi pei shuang ying hao zhi jian de shu zhi
webmainurl = re.findall(r'(.*)/.*?',weburl)
newweburl = ""
newactions= ""
newwebmainurl=""
for index in range(len(chunaction)):
	newactions=chunaction[index]
	newwebmainurl=webmainurl[index]
newweburl=newwebmainurl+newactions
print "NEW GOAL URL :",newweburl
myweb.webposturl=newweburl
#*******************END NEW URL**************************
#START ATTACK********************************************
#ATTACK CODE*********************************************
#dai ma zan shi fang zai zhe ,yi zi you zhi xing*********
#creat map for post
listTS=dirformn[int(num)]
for index in range(len(listTS)):
	mylistt=re.findall(r'name="(\S*)"',listTS[index])
	postmap[index]=mylistt[0]
file_direct = open('webshell.txt')#zi dian wen jian
for line in file_direct:
	for x in range(len(postmap)):
		str=postmap[x]
		postmup[str]=line
	print "POST :",postmup
	myweb.webpost(postmup)
	postmup.clear()
print "ATTACK END"












