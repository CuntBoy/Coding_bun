# 阶乘 
def factorial(num):
    res = 1
    times = num
    if num in [0, 1]:
        return 1
    else:
        for i in range(num):
            if times == 1:
                return res
            res = res * times
            times = times -1
def Exponentiation(num, n):
    return num ** n


def main():
    mean = int(input("你要计算的是阶乘还是幂？\n 1，阶乘 \n 2, 幂 \n "))
    if mean == 1:
        num = int(input("你要计算谁的阶乘：\n"))
        res = factorial(num)
    else:
        num = int(input("你要计算谁的幂：\n"))
        n = int(input("计算它的多少次幂：\n"))
        res = Exponentiation(num, n)
    print(res)

if __name__ == "__main__":
    main()