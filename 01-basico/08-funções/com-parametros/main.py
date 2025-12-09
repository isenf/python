# com um parametro

def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Python")

# com parametros posicionais
def calc_pagamento(hora, val_hora):
    return hora * val_hora

pagamento = calc_pagamento(2, 75)

print(pagamento)

# com parametros padrão
def despedida(nome="Visitante"):
    print(f"Adeus, {nome}")

despedida() # usa o valor padrão
despedida("Dev")

# parametros arbitrários (*args) -> quantos parametros quiser
def calc_somatorio(*nums):
    return sum(nums)

somatorio = calc_somatorio(1, 3, 5, 7, 9)
print(somatorio)

# parametros de palavra-chave **kwargs (keyword arguments)
def criar_conta(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

criar_conta(nome="Ana", idade=25, cidade="SP")
