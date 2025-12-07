fib = [1, 1, 2, 3, 5, 8, 13, 21, 34]

# enumerate(iterable, inicio), inicio é opcional
for indice, num in enumerate(fib, 1):
    print(f"{indice}º elemento: {num}")