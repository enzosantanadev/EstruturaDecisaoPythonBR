nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))

def funcao(nota1, nota2):
    return (nota1 + nota2) / 2

resultado = funcao(nota1, nota2)

if resultado == 10:
    print("boaaaa vc tirou nota maxima")

elif resultado < 6:
    print("vc foi reprovado estuda mais mano")

else:
    print("parabens vc foi aprovado")

