# Duplicate removal
# coding=utf-8
def main():
    nums = [1, 2, 3, 5, 9, 8, 4, 5, 6]
    nums = list(set(nums))
    print(nums)

if __name__ == "__main__":
    main()