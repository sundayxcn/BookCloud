body = open("suren.html", "r").read().decode('gbk')

# url = "http://www.baidu.com/s?q1= &q2=&q3=&q4=&gpc=stf&ft=&q5=1&q6=www.bxwx9.org&tn=baiduadv";
# url2 = "http://www.baidu.com"
# response = requests.get("url")
# encode = requests.utils.get_encodings_from_content(response.content)
# response.encoding = encode[0]
# response = urllib2.urlopen(url)

def getHtml():
    return body