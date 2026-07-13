num = int(input("Digite um número inteiro positivo: "))

binario = ""

while num > 0:
    resto = num % 2
    binario = str(resto) + binario
    num = num // 2
print("seu numero esta assim em binario: ", binario)
