# -*- coding: utf-8 -*-

def allUrl():
 start_urls = []
 f = open("urls.txt", "r+")
 # 调用文件的 readline()方法
 lines = f.readlines()
 start_urls.extend(lines)
 for line in start_urls:
    line.strip('\n')

 print start_urls
 f.close()
 return start_urls
