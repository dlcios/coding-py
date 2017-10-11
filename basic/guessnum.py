#coding: utf-8
import random

answer = random.randint(1,100)

def guessNum(chance = 7):
    if chance <= 0:
        print("机会被用完啦，别灰心，下次一定能猜中的")
        exit()

    print("你还剩下 %s 次机会可用,加油" %(chance))

    inputNum = input("请输入一个数，数值介于1-100:")

    if inputNum == 'exit':
        print("感谢参加游戏，期待再次相会^_^")
        exit()

    if not inputNum.isdigit():
        print("输入非法,请重新输入")
        guessNum(chance)

    inputnum2 = int(inputNum)

    if inputnum2 < 1 or inputnum2 > 100:
        print("请输入一个介于1-100的正整数")
        guessNum(chance)
    
    if inputnum2 == answer:
        print("恭喜你，猜中啦，答案就是 %d" %(answer))
        exit()
    elif inputnum2 > answer:
        print("还差一点就答对啦，猜的数字比答案大一点哦")
        guessNum(chance -1)
    elif inputnum2 < answer:
        print("还差一点就答对啦，猜的数字比答案小一点哦")
        guessNum(chance -1)

guessNum()
