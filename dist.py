d = {"name":"ming","age":20,"weight":140}
b = dict(type = 1, message = 'ok', url = 'www.baidu.com')
print(d)
print(b)

list1 = [1,2,3]
list2 = [4,5,6,7]
dict2 = dict(zip(list1,list2))
print(dict2)
print(d['name'])
print(d.keys())
print(d.values())
print(d.items())
d_update = dict(name = "yao")
d.update(d_update)
print(d)
del d["weight"]
print(d)
d.clear()
print(d)