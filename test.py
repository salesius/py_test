#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import string

section2 = [
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

section = [ "<id>",
	"<title>",
	"<author>",
	"<pages>",
	"<abstract>",
	"<eauthor>",
	"<eabstract>",
	"<classification>",
	"<keywords>",
	"<notes>"
	""
]

#f = open("one.kt", "r")

#line = f.readline()
#while True:

w = open("result.json", "w")
w2 = open("result2.json", "w")
s_num = 0
l_count = 0

out=["","","","","","","","","","",""]

with open("one.kt", "r") as f :
	for line in f :
		s_check = line.find(section[s_num])
		
	
		if s_check != -1 :
			if s_num == 0 :
				w.write("{")
	
			if s_num != 0 :
				w.write(",")

			temp = section[s_num]
			w.write("\"")
			w.write(temp[1:len(temp)-1]+"\""+":")

			print "num : ", s_num
			print line[len(temp):]
#content = line[len(temp):].strip("\n").strip("\t")
			content = line[len(temp):].translate(None, "\t\n")
			print "content : ", content
			if s_num == 0 :
				w.write(str(int(content)))
				out[s_num] = str(int(content))
			else :
				w.write(content)
				out[s_num] = content
#w.write(line[len(temp):].strip("\n"))
			print line;
			s_num = s_num+1
		else :
			print line + "========="
			w.write(line.strip("\n"))
			# index값을 -1 줘야하는것을 잏지 말자
#out[s_num-1] = out[s_num-1] + line.strip("\n").strip("\t")
			out[s_num-1] = out[s_num-1] + line.translate(None, "\t\n")
		if s_num == len(section): 
			s_num = 0
			w.write("}\n")

			#write file 2
			w2.write("{")
			num=0
			for tt in out :
				w2.write("\"")	
				temp2 = section[num]
				w2.write(temp2[1:len(temp2)-1]+"\""+":")
				if num == 0 :
					w2.write(tt)
					w2.write(",")
				else :
					w2.write("\"")	
					w2.write(tt)
					w2.write("\"")	
					if num != len(section)-1 :
						w2.write(",")

				num = num+1
				if num == len(section) :
					num = 0
					break
				
			w2.write("}\n")
			#end file 2
	
		l_count = l_count + 1

