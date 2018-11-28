# -*- coding: utf-8 -*-
'''
批量翻译
'''

#python3.6.5
# coding=utf-8
#Strong by 20180810

from hashlib import md5
from urllib import request
import random
import xlrd
import json


def fanyi(mes):
    appid = ''  # 你的appid
    secretKey = ''  # 你的密钥

    httpClient = None
    myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate' #api接口
    q = mes.replace(" ", "").replace("&", "")  #去除url中不符合的字符
    print(q)   #打印需要翻译的单词
    fromLang = 'en' #英语
    toLang = 'zh'  #中文
    salt = random.randint(32768, 65536) #生成随机数

    sign = (appid + q + str(salt) + secretKey) #密钥
    m1 = md5() #创建hash5
    m1.update(sign.encode("utf-8"))
    sign = m1.hexdigest() #生成加密字符串
    myurl2 = myurl + '?appid=' + appid + '&q=' + q + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign
    # print(myurl2.replace(" ",""))
    req = request.Request(myurl2)#请求接口
    try:
        s = request.urlopen(req) #请求接口
    except Exception as e:
        print(e)
        return {"src": mes, "dst": mes}
    m = s.read().decode("utf-8")
    js = eval(m) 
    #生成字典
    print(js)
    trans_result = js["trans_result"]  
    #取值
    l = str(trans_result).strip("[").strip("]") 
    #洗数据
    a = eval(l) 
    #生成字典

    return a  #返回


def read():
    file_path = r'I:\1.xls'  #读取文件路径
    # 读取的文件路径
    # file_path = file_path.decode('ANSI')
    # 文件中的中文转码
    data = xlrd.open_workbook(file_path)   
    #打开excel文件 获取数据
    table = data.sheet_by_name('Sheet1')
    # 获取sheet
    nrows = table.nrows
    # 获取总行数
    ncols = table.ncols
    # 获取总列数

    f = open("D:/fanyi.xls", "w") 
     #将翻译好的数据写入这个文件
    er = open("D:/fanyicuowu.xls", "w") 
    #遇到错误写道这个文件里面
    print("行数", nrows)
    print("列数", ncols)
    for i in range(2, nrows, 1):
        for j in range(0, 4, 1):
            # print("i",i,"j",j)
            cell_value = table.cell(i, j).value  
            #去除单元格的值
            # print(cell_value)
            if cell_value == "":
                pass
            #     print("kkkkkkk")
            #     break
            else:
                print("i",i,"j",j,cell_value)
                a = fanyi(cell_value)   #翻译
                try:
                    f.write(a["src"] + "\t") 
                     #写入文件
                    f.write(a["dst"] + "\n")  
                    #写入文件
                except Exception as u:
                    print(u)
                    er.write(u + "\t")   
                    #将错误写入文件
                    er.write(cell_value + "\n") 
                    #写入出错的单词

    er.close()
    f.close()
    return None
if __name__ == '__main__':
    read()