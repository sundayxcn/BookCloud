#!/usr/bin/env python
# coding:utf-8
import os

# 本地文件调试中
BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, 'suren.html')
body = open(file_path, "r").read().decode('gbk')


# url = "http://www.baidu.com/s?q1= &q2=&q3=&q4=&gpc=stf&ft=&q5=1&q6=www.bxwx9.org&tn=baiduadv";
# url2 = "http://www.baidu.com"
# response = requests.get("url")
# encode = requests.utils.get_encodings_from_content(response.content)
# response.encoding = encode[0]
# response = urllib2.urlopen(url)

def get_html():
    return body
