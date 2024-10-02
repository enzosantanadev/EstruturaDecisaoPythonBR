
preco1 = float(input("digite o preço do produto 1: "))
preco2 = float(input("digite o preço do produto 2: "))
preco3 = float(input("digite o preço do produto 3: "))

if preco1 < preco2 and preco1 < preco3:
    print("vc deveria comprar o produto 1")

elif preco2 < preco1 and preco2 < preco3:
    print("vc deveria comprar o produto 2")
else:
    print("vc deveria comprar o produto 3")
