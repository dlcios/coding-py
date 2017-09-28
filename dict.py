#coding: utf-8
#字典查找速度极快但是消耗内存较多

dict1 = {"name": "Machel", "age": 26, "sex": "male"}

print(dict1['name'])

if 'name1' in dict1:
    dict1['name'] = 'Micheal'
else:
    dict1['name1'] = 'emmmm'

print(dict1)