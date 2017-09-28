#列表查找和插入随着元素量增多变慢，但相对字典消耗内存很少
a = [1,2,3]
b = [3,5,7]
c = [1,2,3]

a_copy = a
b_copy = a
c_copy = b

print(len(a))
print(a[0],b[2])
a.insert(0,2)
print(a)

print(id(a))
print(id(b))
print(id(c))
print(id(a_copy))
print(id(b_copy))
print(id(c_copy))

print(a.count(1))

a_copy.append(1);

print(a)

a.pop()
print(a)

a.reverse()

print(a)

# 元组 不可变列表
x = (1,2,3)
x_copy = x

print(id(x))
print(id(x_copy))
print(x_copy)

