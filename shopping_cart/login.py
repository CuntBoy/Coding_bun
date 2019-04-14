# coding:utf-8

users = [
    {"id": "1234569", "username": "潘圆明", "password": "12345678", },
    {"id": "1234567", "username": "陈磊宇", "password": "12345678", },
    {"id": "1234568", "username": "张大扬", "password": "12345678", },
]

user_id_lists = list()
for i in users:
    user_id_lists.append(i['id'])

judge = False

def wellcome_to_here():
    print("欢迎进入OOXX购物商城.")



def usr_login():
    while True:
        try:
            user_id = input("输入你的id：")
            if user_id in user_id_lists:
                password = input("请输入密码:　")
                for i in users:
                    j = i
                    if j['id'] == user_id:
                        while True:
                            if password == j["password"]:
                                print("认证成功")
                                judge = True
                                break
                            else:
                                print("请重新输入")
                                password = input("请输入密码：")
                                continue
                    else:
                        continue
                    if judge:
                        break
                if judge:
                    break
            else:
                raise KeyError("用户不存在，请注册")
        except Exception as e:
            print(e)

        # 转到注册账户的页面 
        # 此处未作要求 不实现
    print("欢迎来到, 冉氏购物商城,祝您购物愉快!")




