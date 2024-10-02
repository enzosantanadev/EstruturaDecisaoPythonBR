num1 = float(input("digite o valor 1: "))
num2 = float(input("digite o valor 2: "))
num3 = float(input("digite o valor 3: "))

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(num1, num2, num3)
    else:
        print(num1, num2, num3)
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print(num2, num1,num3)
    else:
        print(num2, num3, num1)

else:
    if num1 > num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)
