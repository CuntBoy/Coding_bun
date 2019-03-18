# coding=utf-8
# 两层简单神经网络

import tensorflow as tf

# 定义输入, 参数
x = tf.constant([[0.7, 0.5]])   
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))  # 正太分布随机数 标准差 1 随机数种子 1
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))

# 定义前向传播过程
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)


# 使用会话计算结果
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()  # 初始化
    sess.run(init_op)
    print("-->y<-- : \n", sess.run(y))   #输出计算结果








