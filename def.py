#coding: utf-8

# to16mod = hex
# n1 = to16mod(25)
# print(n1)

# #定义函数

# def mabs(num):
#     if num > 0:
#         return num
#     else:
#         return -num

# a = -15
# b = 15

# print(mabs(a), mabs(b))

# def power(x):
#     return x * x

# print(power(a))

# def powern(x,y = 2):
#     s = 1
#     while y > 0:
#         s = s * x
#         y -= 1
    
#     return s

# print(powern(2,1))

def add_append(l=None):
    if l == None:
        l = []
    l.append('hello')
    return l

print(add_append([1,2]))
print(add_append([3,4]))

print(add_append())
print(add_append())


