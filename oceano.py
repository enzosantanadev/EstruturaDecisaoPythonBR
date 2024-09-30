num1 = float(input("digite um numero: "))
num2 = float(input("digite outro numero: "))
num3 = float(input("digite um terceiro numero: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} é o maior deles")

elif num2 > num3 and num2 > num1:
    print(f"{num2} é o maior deles")

else:
    print(f"{num3} é o maior deles")