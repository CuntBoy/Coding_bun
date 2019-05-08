#coding=utf-8

def serarch(lists, number, lower, upper):
    # print(number)
    if lower == upper:
        assert number == lists[upper]
        return upper
    else:
        middle = (lower + upper) // 2  # 3
        # print(lists[middle])
        if lists[middle] == number:
            # print(lists[middle])
            return middle
        if number > lists[middle]:
            lower = middle + 1
            # print(lists[middle])
            return serarch(lists, number, lower, upper)
        else:
            upper = middle
            # print(lists[middle])
            return serarch(lists, number, lower, upper)


def main():
    ls = [31, 25, 35, 56, 89, 78, 90]
    # ls = range(1, 100, 2)
    lower = 0
    a = -1
    upper = len(ls) - 1
    ls = sorted(ls)
    print(ls)
    try:
        a = serarch(ls, 25, lower, upper)
    except Exception as e:
        if a==-1:
            print(e)
            print("It's have no number in here")
    else:
        print("I find that index is : ")
        print(a)



if __name__ == "__main__":
    # print("hello")
    main()