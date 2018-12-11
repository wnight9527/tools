#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/05/10 21:50


 1import requests
 2import itchat
 3
 4KEY = '8edce3ce905a4c1dbb965e6b35c3834d'
 5
 6def get_response(msg):
 7    # 这里实现与图灵机器人的交互
 8    # 构造了要发送给服务器的数据
 9    apiUrl = 'http://www.tuling123.com/openapi/api'
10    data = {
11        'key' : KEY,
12      'info' : msg,
13      'userid' : 'wechat-robot',
14    }
15    try:
16        r = requests.post(apiUrl, data=data).json()
17        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
18        return r.get('text')
19    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
20    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
21    except:
22        # 将会返回一个None
23        return
24
25# 这里实现微信消息的获取
26@itchat.msg_register(itchat.content.TEXT)
27def tuling_reply(msg):
28    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
29    defaultReply = 'I received: ' + msg['Text']
30    # 如果图灵Key出现问题，那么reply将会是None
31    reply = get_response(msg['Text'])
32    # a or b的意思是，如果a有内容，那么返回a，否则返回b
33    # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试
34    return reply or defaultReply
35
36# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
37itchat.auto_login(hotReload=True)
38itchat.run()