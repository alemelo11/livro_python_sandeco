'''Implemente uma função chamada maior_numero() que receba três números como
 parâmetros e retorne o maior deles. Teste a função com diferentes entradas e exiba o
 maior número. 
 '''
# Função que retorna o maior de três números

def maior_numero(a, b, c):
    if b < a > c:
        return a
    elif a < b > c:
        return b
    else:
        return c


# Testando a função com diferentes entradas
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = maior_numero(num1, num2, num3)
print(f"O maior número é: {maior}")



