import numpy as np

with open('feiyong.txt', 'r') as a:
    x = a.read()

data = eval(x)
s = 0
c = 0
N = 10000  # 随机仿真次数
for j in range(N):  # 蒙特卡洛仿真
    xing1 = data[0] * 24  # 一费牌24张
    xing2 = data[1] * 21
    xing3 = data[2] * 18
    fapaishu = 5 * 8
    choose_result = []
    for i in range(fapaishu):
        choose_xingji = np.random.choice([xing1, xing2, xing3], p=[0.5, 0.3, 0.2])
        choose = np.random.choice(choose_xingji)
        # if i < 5:  # 0~4认为是第一位玩家的牌
        choose_xingji.remove(choose)
        choose_result.append(choose)
        # print(choose)

    first_pai = choose_result[5:10]
    zhenying = [i.split(' ')[3] for i in first_pai]
    # print(zhenying)
    m = zhenying.count('长安')
    s += m
    if m > 0:
       c += 1
pass
print('平均第一轮五张牌出现长安牌的期望为：', s / N)
print('平均第一轮五张牌出现长安牌的概率为：', c / N)
# x = [choose_result.count(i) for i in choose_result]
# print(max(x))
