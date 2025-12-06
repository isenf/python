# int() converte variável (ou valores) de outros tipos para int
a = '1'
b = int(a)
c = 0.2
d = int(c)

print(f"a -> {a} {type(a)}\nb -> {b} {type(b)}\nc -> {c} {type(c)}\nd -> {d} {type(d)}")

# float() converte para tipo float
e = 10
f = float(e)
g = float('2')

print(f"e -> {e} {type(e)}\nf -> {f} {type(f)}\ng -> {g} {type(g)}")

# str() converte para string
h = 123
i = str(h)

print(f"h -> {h} {type(h)}\ni -> {i} {type(i)}")
