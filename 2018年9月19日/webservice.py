import suds
from suds.client import Client
     
url = "http://192.168.5.23/wstopprd/ws/r/awsp900?WSDL"     # WSDL文件
client = Client(url)
a = __doc__
print(client)   #获取所有的接口函数
result = client.service.getHealthyHeBei(a)     #发送请求   GetOnlineUser为函数
print(result) #打印结果