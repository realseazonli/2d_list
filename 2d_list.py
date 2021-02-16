# 二维清单

products = []
while True :
    name = input('请输入商品名称：')
    if name == 'q' :
        break
    price = input('请输入商品价格：')
    products.append([name, price])
print(products)

for p in products :
    print(p[0], '的价格是', p[1])

with open('products.csv', 'w') as f :
    for p in products :
        f.write(p[0] + ',' + p[1] + '\n')
with open('products.csv', 'r') as f :
    for line in f :
        print(line)