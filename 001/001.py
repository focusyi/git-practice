#!/usr/bin/env python
#coding:utf-8

import string
import random

word = string.uppercase  #返回所有大写
number = string.digits   #返回所有小写

words = word + number

for i in range(1,200):
    yanzheng = ''
    for m in range(10):
        num = random.randint(0,35)
        yanzheng += words[num]
    with open('1.txt','a') as fb:
        fb.write(yanzheng+'\n')

