'''
Desenvolva uma função chamada contar_vogais() que receba uma string como 
parâmetro e retorne o número de vogais presentes nessa string. Utilize essa 
função para contar o número de vogais em uma frase fornecida pelo usuário.
'''

def contar_vogais(frase):
    # Função que conta o número de vogais em uma string
    num_vogais = 0
    for letra in frase:
        if letra.lower() in 'aeiou':
            num_vogais = num_vogais + 1
    return num_vogais

frase = input("Digite uma frase: ") 
print(f'A frase: "{frase}" tem {contar_vogais(frase)} vogais')