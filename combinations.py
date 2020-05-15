"""
Combinations, Permutations e Product - Itertools
"""

print('\nCombinação - Ordem não importa')
from itertools import combinations

names = ['Luiz', 'Maria', 'David', 'Alberto', 'Rose', 'Fernanda']

for group in combinations(names, 2):
    print(group)

print('\nPermutação - Ordem importa')
from itertools import permutations

names = ['Luiz', 'Maria', 'David', 'Alberto', 'Rose', 'Fernanda']

for group in permutations(names, 2):
    print(group)

print('\nProduto - Ordem importa e repete valores únicos')
from itertools import product

names = ['Luiz', 'Maria', 'David', 'Alberto', 'Rose', 'Fernanda']

for group in product(names, repeat=2):
    print(group)