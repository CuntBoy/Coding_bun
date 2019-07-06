# coding = utf-8
# 函数实现求斐波拉契数列前十项  

def febo():
    a, b = 0, 1
    febo_list = []
    for i in range(10):
        febo_list.append(b)
        a, b = b, a+b
    
    return febo_list


def main():
    febo_list = febo()
    print(febo_list)

if __name__ == "__main__":
    main()