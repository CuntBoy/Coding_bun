# coding=utf-8

import pandas as pd
import numpy as np

# 核心代码，设置显示的最大列、宽等参数，消掉打印不完全中间的省略号
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

# 设置文件路径
file_path = "./starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)
print(df.head(5))  #输出所打开文件的前5行
print(df.info())   #查看文档信息 

# 分组 把文件按照国家分组
grouped = df.groupby(by="Country")
# print(grouped)  # 输出分组后的内容

# DataFrameGroupBy 分组后得到的数据类型
# 1, 可以遍历
# for i, j in grouped:
#     print(i)
#     print("-"*50)
#     print(j)
#     print("=" * 50)
# 2, 可以聚合
# print(grouped["Brand"].count())

# 统计数据中美国和中国的星巴克数量
country_count = grouped["Brand"].count()
print(country_count["US"])
print(country_count["CN"])
