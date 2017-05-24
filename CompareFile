#!/usr/bin/python
import sys
import difflib

def readfile(filename):
# '''
# read file content
# '''
    f=open(filename,'rb')
    content=f.readlines()
    return content
file1=readfile(sys.argv[1])
file2=readfile(sys.argv[2])

d=difflib.HtmlDiff()
print d.make_file(file1,file2)
with open('result.html','wb') as f:
    f.write(d.make_file(file1,file2))
