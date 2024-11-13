'''Escreva uma função chamada calcular_potencia() que receba dois parâmetros,
base e expoente, e retorne o resultado da base elevada ao expoente. Utilize a função
para calcular a potência de números fornecidos pelo usuário.
'''
# def calcular_potencia(base, expoente):
#     return base ** expoente


# # Testando a função com diferentes entradas
# num = int(input("Digite um numero: "))
# num2 = int(input("Digite outro numero: "))
# potencia = calcular_potencia(num, num2)
# print(f"{num} elevado à {num2} é {potencia}")
###############################################################################


''' 
 Crie uma função chamada converter_segundos() que receba um valor em segundos
 e o converta para o formato horas, minutos e segundos. A função deve retornar uma
 string formatada como "X horas, Y minutos e Z segundos". Teste a função com diferentes
 entradas.
 '''
# def converter_segundos(segundos):
#     horas = segundos // 3600
#     minutos = (segundos % 3600) // 60
#     segundos = (segundos % 3600) % 60
#     return f"{horas} horas, {minutos} minutos e {segundos} segundos"    

# # Testando a função com diferentes entradas
# segundos = int(input("Digite um número de segundos: "))
# resultado = converter_segundos(segundos)
# print(resultado)        
########################################################################################


'''
implemente uma função chamada calcular_hipotenusa() que receba os 
 comprimentos dos dois catetos de um triângulo retângulo e retorne o comprimento da hipotenusa,
 usando o teorema de Pitágoras. Utilize a função para calcular a hipotenusa com valores
 fornecidos pelo usuário.
'''
# def calcular_hipotenusa(a, b):
#     c = (a ** 2 + b ** 2) ** 0.5
#     return c

# # Testando a função com diferentes entradas    
# num = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# hipotenusa = calcular_hipotenusa(num, num2)
# print(f"O comprimento da hipotenusa é {hipotenusa}")
############################################################################################

'''Desenvolva uma função chamada eh_primo() que receba um número inteiro e retorne
True se o número for primo e False caso contrário. Utilize a função para verificar se um
número fornecido pelo usuário é primo.
'''
# def eh_primo(numero):
#     if numero <= 1:
#         return False
#     for divisor in range(2, int(numero ** 0.5) + 1):
#         if numero % divisor == 0:
#             return False
#     return True

# # Testando a função com diferentes entradas
# num = int(input("Digite um número: "))
# if eh_primo(num):
#     print(f"{num} é primo")
# else:
#     print(f"{num} não é primo") 
#################################################################################

'''
Desenvolva uma função chamada inverter_lista() que receba uma lista como parâmetro e retorne
uma lista invertida. Utilize a função para inverter uma lista de números fornecida pelo usuário.
'''
# def inverter_lista(numeros):
#     lista_invertida = numeros[::-1]
#     return lista_invertida

# numeros_usuario = list(map(int, input("Digite uma lista de números, separados por espaço: ").split()))
# resultado = inverter_lista(numeros_usuario)
# print("Lista invertida:", resultado)
##########################################################################################3


'''
Crie uma função chamada fibonacci_ate() que receba um número inteiro n e retorne
uma lista contendo todos os números da sequência de Fibonacci até n. Utilize a função
para gerar a sequência de Fibonacci até um valor fornecido pelo usuário
# '''
# def fibonacci_ate(n):
#     if n < 0:
#         return []
#     if n == 0:
#         return [0]
#     elif n == 1:
#         return [0, 1]

#     sequencia = [0, 1]

#     while True:
#         proximo = sequencia[-1] + sequencia[-2]
#         if proximo > n:
#             break
#         sequencia.append(proximo)

#     return sequencia

# n = int(input("Digite um número para gerar a sequência de Fibonacci até esse valor: "))
# print("Sequência de Fibonacci até", n, ":", fibonacci_ate(n))
# print(f'Sequência de Fibonacci até {n}: {fibonacci_ate(n)}')
################################################################################33333333











