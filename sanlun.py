import numpy as np

with open('feiyong.txt', 'r') as a:
    x = a.read()

data = eval(x)

N = 1000  # 随机仿真次数
lunci = 3
# 假设每人都不抢长安
fapaishu = 40 * 3
choupailunci = 2


for choupailunci in range(10):
    s = 0
    c = 0
    choupaishu = choupailunci * 5
    for j in range(N):  # 蒙特卡洛仿真
        xing1 = data[0] * 24  # 一费牌24张
        xing2 = data[1] * 21
        xing3 = data[2] * 18

        choose_result = []
        for i in range(fapaishu):
            choose_xingji = np.random.choice([xing1, xing2, xing3], p=[0.5, 0.3, 0.2])
            choose = np.random.choice(choose_xingji)
            # if i < 5:  # 0~4认为是第一位玩家的牌
            if choose.split(' ')[3] == '长安':
                choose_xingji.remove(choose)
            choose_result.append(choose)
            # print(choose)

        first_pai = []

        for i in range(lunci):
            first_pai += choose_result[i * 40: i * 40 + 5]

        for i in range(choupaishu):
            choose_xingji = np.random.choice([xing1, xing2, xing3], p=[0.5, 0.3, 0.2])
            choose = np.random.choice(choose_xingji)
            # if i < 5:  # 0~4认为是第一位玩家的牌
            # if choose.split(' ')[3] != '长安':
            choose_xingji.remove(choose)
            first_pai.append(choose)

        zhenying = [i.split(' ')[3] for i in set(first_pai)]
        # print(zhenying)
        m = zhenying.count('长安')
        s += m
        if m > 2:
            c += 1
    pass
    # print('平均第三轮十五张牌出现长安牌的期望为：', s / N)
    print('平均多抽' + str(choupailunci) + '轮牌凑成三长安的概率为：', c / N)
# x = [choose_result.count(i) for i in choose_result]
# print(max(x))
