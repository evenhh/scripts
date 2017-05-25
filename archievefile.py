#!/usr/bin/env python
#coding=utf-8
'''

文件的压缩以及解压

@author: liuzhe
'''
import tarfile
import os

archivefile = tarfile.open('D:\download.tar.gz','w:gz')  #open函数类似于普通文件,r,w,a,可额外指定压缩格式，'w:gz' 表示创建gz格式压缩包 
for rootdir ,subdirs,files in os.walk('D:\downloads'):
    for f in files:
        archivefile.add(os.path.join(rootdir,f),arcname=f) ##arcname  自定义打包后的文件名
archivefile.close()

uncompressfile = tarfile.open('D:\download.tar.gz','r:gz')
for files in uncompressfile:
    print files.name
    if  files.name == '5.jpg' or True:
        uncompressfile.extract(files,path='E:\\ftp')  #解压文件，并指定目录，不指定目录则解压到当前目录
uncompressfile.close()
