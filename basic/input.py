#coding: utf-8

birth = input("请输入年龄:")
birth = int(birth)
if birth < 2000:
    print("00前")
else:
    print("00后")