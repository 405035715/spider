import urllib.request

response = urllib.request.urlopen('http://www.baidu.com/')
html = response.read()
print(html)
print(response.geturl())
print(response.info())

