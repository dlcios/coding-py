#coding: utf-8
l1 = [1,2,3,4]
l2 = ['php', 'c', 'java', 'go']
l3 = [4,3,2,1]

tup1 = (l1, l2)

print(tup1)

#元祖的元素不可变指的是指向地址不可变
tup1[0][0] = 5

tup1[1][2] = 'c++'

print(tup1)

tup1[0] = l3
print(tup1)