# escopo de variáveis: local ou global

# local: dentro da função
def imprime_10():
    x = 10 # variável local
    print(x)

imprime_10()


# global: acessadas em qlqr parte do programa
y = 25

print(f"y antes: {y}")

def mod_dobro():
    global y # necessário para modificar a variável global
    y = y * 2

mod_dobro()
print(f"y depois: {y}")