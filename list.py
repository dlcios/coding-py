#列表
a = [1,2,3]
b = [3,5,7]
c = [1,2,3]

a_copy = a
b_copy = a
c_copy = b

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

