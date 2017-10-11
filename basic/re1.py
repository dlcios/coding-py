#coding: utf-8

import re

t = "c++ python2 python3 perl ruby lua java javascript php4 php5 c"
print(re.match(r"java", t))
print(re.search(r'java', t))
print(re.match(r'c\+\+', t))

print(re.findall(r'python',t))
print(re.split(r'perl', t))
print(re.sub('ruby','fortran', t))

print(re.findall('p+',t))
print(re.findall('p[a-zA-z]+',t))
print(re.findall('p[a-zA-z]*',t))
print(re.findall('p[a-zA-z]?',t))
print(re.findall('p[a-zA-z0-9]{3,}',t))
print(re.findall('[pj][a-zA-z0-9]*',t))

# \w [a-zA-Z0-9_]
# \d [0-9]
# \s [\s\n\r\f\v]

