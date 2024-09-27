from traceback import print_tb

a = float(input("digite um valor: "))

if a < 0:
    print(f"{a} é um valor negativo")

elif a > 0:
    print(f"{a} é um valor positivo")

else:
    print(f"{a} é zero")
