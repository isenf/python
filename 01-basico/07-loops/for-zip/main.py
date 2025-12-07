nomes = ["Ana", "Beatriz", "Carla"]
idades = [21, 29, 34]

# zip funciona com listas, tuplas, strings e combinações entre eles
for n, i in zip(nomes, idades):
    print(f"{n} tem {i} anos")

meses = ("Janeiro", "Junho", "Dezembro")
n_meses = (1, 6, 12)

for m, n in zip(meses, n_meses):
    print(f"{m} é o {n}º mes do ano")