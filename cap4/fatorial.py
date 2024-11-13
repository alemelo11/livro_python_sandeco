def fatorial(n):
    if n == 0 or n == 1: # Condicao de parada
        return 1
    else:
        return n * fatorial (n - 1) #Chamada recursiva

resultado = fatorial(6)
print(resultado)
