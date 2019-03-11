# coding=utf-8
import random

print("这是一个猜数字的游戏,系统随机生成一个数字(0-100之间),然后你猜")
rand_num = (random.randint(0,100))
# num = eval(input("输入你猜的数字: "))

while True:
    num = eval(input("输入你猜的数字: "))
    if num == rand_num:
        print("恭喜你,猜对了")
        break
    elif num > rand_num:
        print("太大了,小一点,重新输入:")
        continue 
    else:
        print("太小了,大一点,重新输入:")
        continue
    
print("系统随机数是: {}".format(rand_num))
        

