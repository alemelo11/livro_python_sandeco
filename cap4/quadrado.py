'''
Crie uma função chamada quadrado() que receba um número como parâmetro e retorne o quadrado desse número. 
Em seguida, escreva um programa que utilize essa função para calcular e exibir o quadrado de um número fornecido pelo usuário.
'''
# Função que calcula o quadrado de um número
def quadrado(numero):
    return numero ** 2

# Programa que usa a função
numero_usuario = int(input("Digite um número: "))
resultado = quadrado(numero_usuario)
print(f"O quadrado de {numero_usuario} é {resultado}")
