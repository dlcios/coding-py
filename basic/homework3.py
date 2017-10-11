#coding: utf-8
import re

#模拟注册过程,用户输入用户名后进行检测用户名是否存在文件中,并返回合理的错误提示,如果不在则再输入密码,成功则添加用户信息到文件中，密码进行md5加密处理

#增加用户名，密码的合法化判断和错误提示
#用户名：字母，数字，下划线
#密码：字母，数字，下划线和横线,长度不小于6

def register(uname = '', pwd = ''):
    
    if uname == '':
        inputText_name = input("请输入用户名，由字母，数字，下划线组成:")
    else:
        inputText_name = uname

    pattern_name = re.compile(r"^\w{4,}$")

    match_name = pattern_name.match(inputText_name)

    if not match_name:
        print("用户名非法！")
        register()
        return

    if pwd == '':
        inputText_pwd = input("请输入密码，由字母，数字，下划线组成:")
    else:
        inputText_pwd = pwd

    pattern_pwd = re.compile(r"^\w{6,}$")
    match_pwd = pattern_pwd.match(inputText_pwd)

    if not match_pwd:
        print("密码非法！")
        register(inputText_name)
        return

    inputText_pwd2 = input("请再次输入密码以确认:")

    if not (inputText_pwd == inputText_pwd2):
        print("两次输入密码不一致，请重新输入密码确认")
        register(inputText_name,inputText_pwd)
        return

    print("注册成功")

register()


