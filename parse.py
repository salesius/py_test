#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import string
import json

section = [
	"<id>",
	"<title>",
	"<author>",
	"<affiliation>",
	"<uint8-1>",
	"<uint8-2>",
	"<uint16-1>",
	"<uint32-1>",
	"<uint32-2>",
	"<uint64-1>",
	"<float-1>",
	"<float-2>",
	"<float-3>",
	"<muint32>",
	"<mstr>",
	"<score>",
	"<language>",
	"<journal>",
	"<issn>",
	"<year>",
	"<volume>",
	"<number>",
	"<pages>",
	"<abstract>",
	"<etitle>",
	"<eauthor>",
	"<eabstract>",
	"<classification>",
	"<keywords>",
	"<notes>"
] 


listInt = [0,4,5,6,7,8,9,10,11,12,15,19,20,21]

w2 = open("result2.json", "w")
s_num = 0
l_count = 0

out=[None]*len(section)


#with open("one_16", "r") as f :
with open("kt.doc.56", "r") as f :
	for line in f :
		s_check = line.find(section[s_num])

		if s_check != -1 :
			temp = section[s_num]
			content = line[len(temp):].translate(None, "\t\n")

			if s_num == 0 :
				out[s_num] = str(int(content))
			else :
				out[s_num] = content

			s_num = s_num+1

		else :
			out[s_num-1] = out[s_num-1] + line.translate(None, "\t\n")


		if s_num == len(section): 
			s_num = 0
			w2.write("{\"index\":{\"_id\":\"")
			w2.write(out[0])
			w2.write("\"}}\n")

			w2.write("{")
			num=0
			for tt in out :
				w2.write("\"")	
				temp2 = section[num]
				w2.write(temp2[1:len(temp2)-1]+"\""+":")

				#integer인 센션들은 이렇게 처리하기 " 필요없으므로
				if num in listInt :
					w2.write(tt)
					w2.write(",")
				else :
					w2.write("\"")	
					w2.write(tt.replace('"', '\\"'))
					w2.write("\"")	
					if num != len(section)-1 :
						w2.write(",")

				num = num+1
				if num == len(section) :
					num = 0
					break
				
			w2.write("}\n")


		l_count = l_count + 1
