# criar lista

nums = [1, 2, 3, 4, 5]

# acessar
pri_nums = nums[0] # primeiro elemento
ult_nums = nums[-1] # ultimo elemento

# modificar
nums[0] = 7

# append() adiciona ao fim da lista
nums.append(9) 

# insert() adiciona em uma posição escolhida
nums.insert(1, "python")

# remove() remove um valor da lista
nums.remove("python")

# pop() remove e retorna o ultimo elemento
ult_nums = nums.pop()

# len() retorna o tamanho da lista
tamanho = len(nums)

# in verifica se um elemento está presente ou não, retorna True ou False
em_nums = 2 in nums

print(nums)