import os
import codecs

#公交车数据读取，并存入字典
#结果如下
#1(马官营-四惠站) : [马官营,六里桥北里,.....,四惠站],
#1(四惠站-马官营) : [四惠站,八王坟,.......,马官营],
#.
#.
#.

#数据文件有错,无法完成
filePath = 'f:/python/extra_file/beijing_jt.csv'

file = codecs.open(filePath, 'r', 'utf-8')

print(file.read())
file.close()