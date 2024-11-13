def somar(a, b):
    return a + b


def multiplicar(a, b):
    return a * b

def calcular_media_ponderada(n1, n2, peso1, peso2):
    soma_pesos = somar(peso1, peso2)
    total = somar(multiplicar(n1, peso1) , multiplicar(n2, peso2))
    return total / soma_pesos


media = calcular_media_ponderada(7, 8, 4, 2)
print(media)


