# definição
linguagem = {'nome': 'Python', 'versao': 3.13, 'plataforma': 'windows'} # chave: valor

# acesso
nome = linguagem['nome']
versao = linguagem.get('versao') 

# modificação
linguagem['versao'] = 3.14

# adiciona chave valor
linguagem['ano'] = 2025

# remove a chave 
linguagem.pop('ano')

# método para conseguir chaves
chaves = linguagem.keys()

# método para conseguir valores
valores = linguagem.values()

# items: lista de tuplas (chave, valor)
itens = linguagem.items()

print(linguagem)