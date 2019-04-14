# coding=utf-8

products_list = [
	{"id": "1001", "name": "纸巾",   "price": 20},
	{"id": "1002", "name": "剃须刀", "price": 120},
	{"id": "1003", "name": "三只松鼠大礼盒", "price": 190},
]

# 输出商品列表 
def print_products():
	for pros in products_list:
		print("{} 编号: {} 价格: {}元".format(pros["name"],pros["id"], pros["price"]))

# 输入购物卡的余额  然后开始购物 
# user_balance = input("输入你的购物卡余额:")

# 输出商品列表: 
# print_products()

def buy_product(balances):
	# 输入要购买的商品编号
	product_price = 0
	index = False
	pd = False 
	while True:
		product_id = input("输入商品ID: ")
		for li in products_list:
			if product_id == li["id"]:
				product_price = li["price"]
				if (product_price) > balances:
					print("余额不足: 请及时充值, 或换购其他商品")
					pd = True
					print_products()
					print("当前余额为{}".format(balances))
					break 
				else:
					balances = balances - (product_price)
					print("购买成功, 我们将按照您填写的地址进行送货")
					index = True
					break
		if pd == False:
			print("输入错误, 请重新输入")

		if index:
			break

		
			








