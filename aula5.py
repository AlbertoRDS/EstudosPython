lista = [12, 10, 7, 5]
lista_animal = ['cachorro','gato','elefante','lobo','arara']
#print(lista_animal[1])

# for x in lista_animal:
#     print(x)

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)

# print(sum(lista))
# print(max(lista))
# print(min(lista))

# print(max(lista_animal))
# print(min(lista_animal))

# nova_lista = lista_animal * 3
# print(nova_lista)

# if 'lobo' in lista_animal:
#     print('existe um lobo na lista')
# else:
#     print('não existe um lobo na lista. Será incluido.')
#     lista_animal.append('lobo') #append acrescenta um elemento na lista.
#     print(lista_animal)

# lista_animal.pop()     #pop retira o ultimo da lista. mas pode escolhe entre () a posição
# print(lista_animal)

# lista_animal.remove('elefante')
# print(lista_animal)

# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)

lista_animal[0] = 'macaco'
print(lista_animal)

tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)