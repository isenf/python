# com retorno: retorna valor

def somar(a, b):
    return a + b

soma = somar(2, 5)
print(soma)

# python permite retornar mais de um valor
def troca(x, y):
    z = x
    x = y
    y = z
    return x, y

a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))

a, b = troca(a, b)

print(f"Novo valor de A: {a}\nNovo valor de B: {b}")