product = []
while True:
	name = input('請輸入商品名稱：') 
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	product.append([name, price])
print(product)

product[0][0]
