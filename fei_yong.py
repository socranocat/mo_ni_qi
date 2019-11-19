with open('hero_data.txt', 'r') as a:
    x = a.read()

data = eval(x)

xing1 = []
xing2 = []
xing3 = []
xing4 = []
xing5 = []

for item in data:
    fei_yong = item.split(' ')[1]
    for i in range(5):
        if fei_yong == str(i + 1):
            eval('xing' + str(i+1) + '.append(item)')
            break

pass
result = [xing1, xing2, xing3, xing4, xing5]
with open('feiyong.txt', 'w') as x:
    x.write(str(result))
