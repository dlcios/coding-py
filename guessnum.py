#coding: utf-8

stra = "包含中文的string"
print(stra.encode("utf-8"))

strb = b'\xe5\x8c\x85\xe5\x90\xab\xe4\xb8\xad\xe6\x96\x87\xe7\x9a\x84string'

print(len(strb))
print(strb.decode("utf-8"))

name = "Ada"
age = 18
country = "中国"

print("大家好, 我叫%s, 今年%d, 来自%s, 希望大家多多关照" % (name, age, country))