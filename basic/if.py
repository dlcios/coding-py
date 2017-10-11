#coding : utf-8

num = 5 if 2 > 1 else 3

print(num)

x = 1
y = 2
if x == 1 and y == 2:
    print(1,'-','2')
elif x == 2:
    print(2)
else:
    print(3)

z = 100
while z > 10:
    # print(z)
    z -= 1

a = [1,3,4,5,7,9,12,35,41,55,123,551,2315]
a2 = [1]
[a2.append(i) for i in a if not i in a2]
print(a2)

for x in a:
    if x % 2 == 0:
        break
    else:
        print(x)
