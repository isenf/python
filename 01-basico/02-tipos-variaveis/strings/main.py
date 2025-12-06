# declaração de variáveis gerais no python: identificador = valor
nome = 'ada lovelace'

print(nome.title()) # title -> primeira letra de cada palavra maiúscula
print(nome.upper()) # upper -> letras maiúsculas
print(nome.lower()) # lower -> letras minúsculas


# strings podem estar entre '' e "" 
pnome = 'ada'
unome = 'lovelace'
fnome = f"{pnome} {unome}"

print(f"Hello, \n{fnome}") # usar variável no print
print("Hello,", pnome, unome, sep=' ', end='\n\n') # sep -> separador; end -> final


linguagem = '  python  '

print(f'\'{linguagem.rstrip()}\'') # retira o espaço depois
print(f'\'{linguagem.lstrip()}\'') # retira o espaço antes
print(f'\'{linguagem.strip()}\'') # retira ambos os espaços


url = 'https://www.python.org/'
url_nova = url.removeprefix('https://')
print(url, url_nova, sep='\n')