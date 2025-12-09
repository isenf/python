# sintaxe: lambda argumentos: expressao

# um argumento
quad = lambda x: x ** 2
print(quad(5))

# mais de um argumento
soma = lambda a, b: a + b
print(soma(10, 20))

# com outras funções(map, filter, sort, etc)
nums = [2 , 1, 9, 4, 10, 3, 5, 0, 2]
nums_sorted = nums.sort(key= lambda y: y) 
print(nums_sorted)
