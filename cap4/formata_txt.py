def add_asteriscos(texto):
    return f"*** {texto} ***"     

def converter_maisuculas(texto):
    return texto.upper()

def formatar_titulo (texto):
    texto_maiusculas = converter_maisuculas(texto)
    return add_asteriscos(texto_maiusculas)

titulo_formatado = formatar_titulo("relatorio de vendas")
print(titulo_formatado)

