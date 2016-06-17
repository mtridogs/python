#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import random
lattery_file = open('lottery_double.txt')
list_latter=[]#latter right
latter_error=[]#latter error
latter_parper=[]#parper data
try:
     lattery_file_text = lattery_file.read()
finally:
     lattery_file.close()
split_file = lattery_file_text.split('\n')
for line in split_file:
	temp_list=[]
	line_file=line.split()
	for i in range(2,8):
		temp_list.append(line_file[i])
	temp_list.append(1)
	list_latter.append(temp_list)
for index in range(0,300):
	temp=[]
	for i in range(0,7):
		if i==6:
			temp.append(0)
			break
		elif i==5:
			temp.append(random.randint(1,16))
		else:
			temp.append(random.randint(1,33))
	if temp in list_latter:
		i = i -1
		continue
	else:
		latter_error.append(temp)



file_output = open('lattery_data','w+')
for i in list_latter:
	for index in i:
		file_output.write(str(index))
		file_output.write(" ")
	file_output.write('\n')

for i in latter_error:
	for index in i:
		file_output.write(str(index))
		file_output.write(" ")
	file_output.write('\n')
file_output.close()


#parper test data
file_output_par = open('parper_data','w+')
for i in range(0,100000):
	temp=[]
	for i in range(0,6):
		if i==6:
			temp.append(0)
			break
		elif i==5:
			temp.append(random.randint(1,16))
		else:
			temp.append(random.randint(1,33))
	if temp in list_latter or temp in latter_error:
		i = i -1
		continue
	else:
		latter_parper.append(temp)

for i in latter_parper:
	for index in i:
		file_output_par.write(str(index))
		file_output_par.write(" ")
	file_output_par.write('\n')
file_output_par.close()