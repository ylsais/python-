import urllib.request

url = 'https://www.baidu.com'



#url的组成
# https://www.baidu.com/s?wd=周杰伦

#   http/https          www.baidu.com       80/443      s      wd=周杰伦           #
#        协议                主机              端口号      路径      参数          锚点
#http   80
#https  443
#mysql  3306

headers={
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

#因为urlopen方法中不能存储字典  所以headers不能传递进去
#请求对象的制定
#主意 因为参数循序的问题  不能直接写url 和headers  中间还有data 所以我们需要关键字传参
request = urllib.request.Request(url=url,headers=headers)

response=urllib.request.urlopen(request)

content=response.read().decode('utf8')

print(content)

