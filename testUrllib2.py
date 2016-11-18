import urllib.request
import urllib.parse



# 发送请求的表单
def urllib_test03():
    url = 'http://121.40.19.7/api/doctor/login'

    values = {'username': '18072996469',
              'password': '123456'
             }

    data = urllib.parse.urlencode(values)           # 编码工作
    data = data.encode('utf-8')

    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'   #模拟浏览器
    headers = {'User-Agent': user_agent}

    req = urllib.request.Request(url, data, headers)         # 发送请求同时传data表单
    the_page = ''
    try:
        with urllib.request.urlopen(req) as response:  # 接受反馈的信息
            the_page = response.read().decode('utf-8')  # 读取反馈的内容
            # for k,v in response.getheaders():   # 打印HTTP响应头
                # print('%s: %s' % (k, v))
            # print(response.geturl())  #打印重定向的链接
            # print(response.info())  # 打印HTTP响应头
            # print()
            return the_page
    except urllib.request.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        print(e)


if __name__ == '__main__':
    # response = urllib.request.urlopen('http://www.baidu.com/')
    # html = response.read()
    # print(response.geturl())
    # print(response.info())

    html = urllib_test03()
    print(html)
