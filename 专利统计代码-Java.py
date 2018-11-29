#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/05/10 21:50
# @Author  : MJay_Lee
# @File    : python统计行数.py
# @Contact : limengjiejj@hotmail.com

import os
import time
basedir = os.path.dirname(__file__)
filelists = []
# 指定想要统计的文件类型
whitelist = ['java']
#遍历文件, 递归遍历文件夹中的所有
def getFile(basedir):
    global filelists
    for parent,dirnames,filenames in os.walk(basedir):
        #for dirname in dirnames:
        #    getFile(os.path.join(parent,dirname)) #递归
        for filename in filenames:
            ext = filename.split('.')[-1]
            #只统计指定的文件类型，略过一些log和cache文件
            if ext in whitelist:
                filelists.append(os.path.join(parent,filename))
#统计一个文件的行数
def countLine(fname):
    count = 0
    single_quotes_flag = False
    double_quotes_flag = False
    with open(fname, 'rb') as f:
        for file_line in f:
            file_line = file_line.strip()
            # print(file_line)
            # 空行
            if file_line == b'':
                pass
            # 注释 //开头
            elif file_line.startswith(b'//'):
                pass
            # 注释  /* 开头
            elif file_line.startswith(b"/*") and not single_quotes_flag:
                single_quotes_flag = True
            # 注释 中间 和 */ 结尾
            elif single_quotes_flag == True:
                if file_line.endswith(b"*/"):
                    single_quotes_flag = False
            # 注释  /** 开头
            elif file_line.startswith(b"/**") and not single_quotes_flag:
                double_quotes_flag = True
            # 注释 中间 和 **/ 结尾
            elif double_quotes_flag == True:
                if file_line.endswith(b"**/"):
                    double_quotes_flag = False

            # 代码
            else:
                count += 1
                with open('code_count.txt', 'a') as f:
                    try:
                        onetext = str(file_line, encoding="utf-8")
                        f.write('\n')
                        f.write(onetext)
                    except UnicodeDecodeError:
                        pass


        print(fname + '----', count)
        return count

if __name__ == '__main__' :
    startTime = time.clock()
    getFile(basedir)
    totalline = 0
    for filelist in filelists:
        totalline = totalline + countLine(filelist)
    print('\033[43m total lines: \033[0m'.center(20,'-'),totalline)
