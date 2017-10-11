#coding: utf-8

import datetime

a = datetime.date.today()
b = datetime.datetime.now()

print(a.year)
print("%s-%s-%s" %(a.year, a.month,a.day))
