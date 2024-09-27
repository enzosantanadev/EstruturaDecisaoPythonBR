letra = input("digite sua letra: ").lower()

if letra in ['a','e','i','o','u']:
    print(f"{letra} é uma vogal")
else:
    print(f"{letra} é uma consoante")
