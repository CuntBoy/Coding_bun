'''
编写一个程序，输入一个0-100的数，
如果是一个奇数，输出0-100内所有小于这个数的质数，
如果是一个偶数，输出0-100内所有小于该数且除该数余数为4的数，
如果输入的不是0-100内的数，显示“请输入0-100内的数”
'''

# 质数判断算法 若是质数则输出  
def function_2(num):
	print("质数判断")
	for i in range(2,num):
	    for j in range(2,i):
	        if i%j==0:
	            break
	    else:
	        print(i)


# 偶数判断算法 若是则输出 
def function_3(num):
	print("偶数判断")
	for i in range(1,num):
		if i % 4 == 0:
			print(i)


# 判断数字函数
def function_1():
	num = eval(input("输入你的数字要判断得数字:"))
	# print(num)
	if num < 0 or num >100:
		print("请输入0-100内的数")
	# 质数判断	
	if num % 2 == 0:
		function_3(num)
	else:  
	 #偶数判断
		function_2(num)


# 主函数
def main():
    {
    	function_1()
    }


if __name__ == "__main__":
	main()