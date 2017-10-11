import codecs
#codecs 中文支持
# f = codecs.open(filename, mode, encoding)

import os
#文件操作
#os.path.exists(filename)
#os.rename(old,new)
# r 只读  w 覆盖写  a 追加写

path = "f:/python/coding-py/"
fileName = "dist.py"
filePath = path + fileName

# F = open(filePath,'r')
print(os.path.exists(filePath))
f = codecs.open(filePath,'a','utf-8')
f.write(u'#用python做些小事儿\n')
f.write(u'#delicious\n')
f.close()

f = codecs.open(filePath, 'r', 'utf-8')
# ff = open(filePath)
print(f.read())

# print(ff.read()) 
# 报错:UnicodeDecodeError: 'gbk' codec can't decode byte 0x8b in position 405: incomplete multibyte sequence

# shelve库 把文件内容读取到字典中
#Pickle/cPickle库 