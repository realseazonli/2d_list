# 二维清单

products = []
# 检查档案在不在文件夹
import os # 引入作业系统
if os.path.isfile('products.csv'):
    print('找到文件了')
    # 读取清单
    with open('products.csv', 'r', encoding='utf-8') as f :
        for line in f :
            if '商品,价格' in line :
                continue
            name,price = line.strip().split(',')
            products.append([name, price])
    print(products)
else :
    print('文件不存在')

# 追加输入商品价格
while True :
    name = input('请输入商品名称：')
    if name == 'q' :
        break
    price = input('请输入商品价格：')
    price = int(price)
    products.append([name, price])
print(products)
for p in products :
    print(p[0], '的价格是', p[1])

# 数据写入文件
with open('products.csv', 'w', encoding='utf-8') as f :
    f.write('商品,价格\n')
    for p in products :
        f.write(p[0] + ',' + str(p[1]) + '\n')
with open('products.csv', 'r') as f :
    for line in f :
        if '商品' in line :
            continue
        print(line)