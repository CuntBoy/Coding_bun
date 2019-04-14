# coding=utf-8
import Buy_Products
import login
user_balance = -1

def main():
	# 开始登陆 
	login.wellcome_to_here()
	login.usr_login()
	# 输入购物卡的余额  然后开始购物 
	main.user_balance = eval(input("输入你的购物卡余额:"))
	# 输出商品列表: 
	Buy_Products.print_products()
	# 购物过程 
	Buy_Products.buy_product(main.user_balance)
        

# 真正执行的代码, 判断是否在当前函数,若是不在 不执行
if __name__=="__main__":
	main()



