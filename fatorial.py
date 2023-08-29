def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

numero_inserido = int(input("Digite um número para calcular o fatorial: "))
resultado_fatorial = calcular_fatorial(numero_inserido)
print(f"O fatorial de {numero_inserido} é {resultado_fatorial}")
