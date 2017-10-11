import codecs
import os
import hashlib

#从user.txt中读取文件内容，再将其中password进行md5加密然后存入另外一个文件中

filePath = 'f:/python/extra_file/user.txt'
infoPath = 'f:/python/extra_file/userinfo.txt'


if not os.path.exists(filePath):
    f = codecs.open(filePath, 'w', 'utf-8')
    f.close()
 
f = codecs.open(infoPath, 'w', 'utf-8')
f.close()

file = codecs.open(filePath, 'r', 'utf-8')
fw = codecs.open(infoPath, 'a', 'utf-8')

for line in codecs.open(filePath, 'r', 'utf-8'):
    f_list = line.split(':')
    md5_str = hashlib.md5()
    md5_str.update(f_list[-1][1:].encode('utf-8'))
    f_list[-1] = ' ' + md5_str.hexdigest() + '\n'
    new_line = ''.join(f_list)
    fw.write(new_line)

file.close()
fw.close()
