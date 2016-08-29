import urllib.request
import urllib.parse



# 发送请求的表单
def urllib_test03():
    url = 'http://121.40.19.7/api/doctor/login'

    values = {'username': '18072996469',
              'password': '123456'
             }

    data = urllib.parse.urlencode(values)  # 编码工作
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data)  # 发送请求同时传data表单
    the_page = ''
    with urllib.request.urlopen(req)  as response: # 接受反馈的信息
        the_page = response.read().decode('utf-8')  # 读取反馈的内容
        return the_page


if __name__ == '__main__':
    # response = urllib.request.urlopen('http://www.baidu.com/')
    # html = response.read()
    # print(response.geturl())
    # print(response.info())

    html = urllib_test03()
    print(html)
