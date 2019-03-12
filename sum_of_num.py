# coding=utf-8
print("只是一个计算 0-N 的奇数与偶数之和的程序")
num = eval(input("请输入你要计算 0 - M 的 M 的值: "))
even = 0   # 偶数     
odd = 0    # 奇数 

for i in range(num):
    if i % 2 == 1:
        odd += i
    else:
        even += i
print("奇数 {}， 偶数 {} ".format(odd, even))
