#!/usr/bin/env python
#coding:utf-8

import string
import random
import MySQLdb


word = string.uppercase  #返回所有大写
number = string.digits   #返回所有小写

words = word + number

def importData(ip, username,password,yanzheng):
    db = MySQLdb.connect(ip,username,password)  #连接
    cursor = db.cursor() #创建游标
    try:
        cursor.execute('create database if not exists db_pytest') #创建数据库
        db.select_db('db_pytest')
        cursor.execute('create table tb_test3(id int auto_increment primary key,yanzhengma varchar(20))')
    except:
        pass
    cursor.execute("insert into tb_test3(yanzhengma) values('%s')" %yanzheng)
    db.commit()
    cursor.close()
    db.close()




for i in range(1,200):
    yanzheng = ''
    for m in range(10):
        num = random.randint(0,35)
        yanzheng += words[num]
    importData('localhost','root','123456',yanzheng)

    # with open('1.txt','a') as fb:
    #     fb.write(yanzheng+'\n')

