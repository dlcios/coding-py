import re

#验证email的正则表达式，邮箱名可以使英文字母或数字或 -,_ 符号，后巷后缀网址名可以是英文或数字，域名可以使 com,org,edu
#例: chu-tian-shu_1981@heibanke2015.com

# mail = "1905790854@qq.com"
mail = "chu-tian-shu_1981@heibanke2015.com"

pattern = re.compile(r"^[\w\-\,]+@[a-zA-Z0-9]+\.(com|org|edu){1}$")
match = pattern.match(mail)

if match :
    print('ok')
else:
    print('false')