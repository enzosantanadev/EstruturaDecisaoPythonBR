sexo = input("qual seu sexo? (responda em F ou M) ")

if sexo.upper() == 'F':
    print("seu sexo é feminino")
elif sexo.upper() == 'M':
    print("seu sexo é masculino")
elif sexo.upper() == 'NB':
    print("vc é nao binario")
else:
    print("sexo invalido")
