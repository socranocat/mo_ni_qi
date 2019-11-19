from my_utils.utils import *

url = 'https://pvp.qq.com/wzmnz/index.html'
driver = create_chrome()
driver.get(url)

# ------------------------------------------
#  定位各个英雄的数据
# ------------------------------------------


heros = selenium_wait_xpath(driver, '/html/body/div[3]/div/div/div[2]/div')
results = []
for hero in heros[1:]:
    a = hero.text.split(' ')
    name = a[0][:-2]  # 英雄名字
    fei_yong = a[1]
    b = hero.get_attribute('class').split(' ')
    zhi_ye = b[-2]  # 英雄职业
    shi_li = b[-1]  # 英雄势力
    result = ' '.join([name, fei_yong, zhi_ye, shi_li])
    print(result)
    results.append(result)
pass

with open('hero_data.txt', 'w') as x:
    x.write(str(results))
