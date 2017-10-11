#coding: utf-8

import codecs
import random
import os

#利用随机函数产生一个用户的用户名，密码，且利用文件将用户名和密码保存下来
basic = "abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ0123486789_"

length = len(basic) -1

nameLength = random.randint(4,7)
pwLength = random.randint(6,18)

username = ''
password = ''

for i in range(nameLength):
    username += basic[random.randint(0,length)]

for i in range(pwLength):
    password += basic[random.randint(0,pwLength)]

writeLine = u'username: ' + username + ' | password: ' + password + '\n'

filePath = 'f:/python/extra_file/user.txt'

if not os.path.exists(filePath):
    F = codecs.open(filePath, 'w' , 'utf-8')
    F.close()

f = codecs.open(filePath, 'a' , 'utf-8')
f.write(writeLine)
f.close()

