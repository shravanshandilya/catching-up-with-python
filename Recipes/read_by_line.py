#! /usr/bin/python
import sys
file=open(sys.argv[0])
line=file.readline()
num=1
while line :
	print num,"#",line,
	line=file.readline()
	num+=1