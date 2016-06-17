import re
#all_the_text = open('dictionary.txt').read()
#pattern_html = re.compile(r'ctf')  
#re_html=pattern_html.findall(all_the_text)
#print len(re_html)
index=0
for line in open("dictionary.txt"):  
	searchObj = re.search( r'ctf',line,re.M|re.I)
	if searchObj:
		index = index +len(line.strip())
	else:
		continue
print index