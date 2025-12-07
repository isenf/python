i = 0

# else só é excutado se não encontrou um break no while
while(i < 5):
    print(i)
    i += 1
else:
    print("Loop completo sem break")

j = 0
while(j < 10):
    if(j == 8):
        break
    print(j)
    j += 2
else:
    print("Loop não encontrou um break")