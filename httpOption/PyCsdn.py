#! /usr/bin/env python
#coding:utf-8
import urllib.request
import sys
points = 0
if len(sys.argv) > 1:
    points = int(sys.argv[1])
    aritcleUrl = 'http://blog.csdn.net/abc649395594/article/digg?ArticleId=47086751'
    point_header = {'Accept': '*/*', 'Cookie': 'your cookie', 'Host': 'blog.csdn.net',
                'Referer': 'http://blog.csdn.net/abc649395594/article/details/47086751',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36'}
    for i in range(points):
        point_request = urllib.request.Request(aritcleUrl, headers=point_header)
        point_response = urllib.request.urlopen(point_request)
