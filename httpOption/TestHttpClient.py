#! /usr/bin/env python
#coding:utf-8
import urllib.request
import json

if __name__ == "__main__":
    restUri = "https://lxxx";
    PostParam = "data=123456"
    DATA = PostParam.encode('utf8')
    req = urllib.request.Request(url=restUri, data=DATA, method='POST')
    req.add_header('Content-type', 'application/x-www-form-urlencoded')
    r = urllib.request.urlopen(req).read()
    print(r.decode('utf8'))
    org_obj = json.loads(r.decode('utf8'))
    print(org_obj['token'])