# Even numbers
# coding=utf-8
import numpy as np 

def Even_numbers(nums):
    Even_list = []
    for i in nums:
        if i % 2 == 0:
            Even_list.append(i)
    return np.sum(Even_list)


def main():
    nums = list(range(1, 101))
    num_sum = Even_numbers(nums)
    print(num_sum)

if __name__ == "__main__":
    main()


