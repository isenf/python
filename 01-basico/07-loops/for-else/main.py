lista = [1, 2, 3, 4, 5]

# else só é executado se não encontrar break no loop for
for i in lista:
    print(i)
else:
    print("Saiu do loop sem encontrar break")


# se encontrar break, sai do loop e não executa o else
for i in lista:
    if(i == 3):
        break
    print(i)
else:
    print("Saiu do loop sem break")