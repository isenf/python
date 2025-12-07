# criação de um set
conj = {1, 2, 3, 3, 4, 5, 5} # elimina elementos repetidos
conj_vazio = set() # cria um conjunto vazio

# adiciona um elemento 
conj.add(5)

# remove um elemento, pode dar KeyError
conj.remove(1)

# remove sem erros
conj.discard(9)

# remove todos os elementos
conj.clear()

# set() pode ser usado em strings
print(set('cachorro'))

# set permite operações de conjuntos
a = {1, 2, 3}
b = {2, 3, 4}

# uniao -> | ou union()
print(a | b)
print(a.union(b))

# interseção -> & ou intersection()
print(a & b)
print(a.intersection(b))

# diferença -> - ou difference
print(a - b)
print(a.difference(b))

# diferença simétrica -> ^ ou symmetric_difference
print(a ^ b)
print(a.symmetric_difference(b))