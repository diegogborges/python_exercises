from dados import products, students, my_list
from functools import reduce

acumula = 0

#acumular sem reduce
for item in my_list:
    acumula += item
print(acumula)

print()
sum_list = reduce(lambda ac, i: i + ac, my_list, 0)
print(sum_list)

print()
sum_price = reduce(lambda ac, p: p['price'] + ac, products, 0)
print(sum_price)
print(f'Price average: {sum_price / len(products)}')

sum_ages = reduce(lambda ac, p: ac + p['age'], students, 0)
print(f'Age average: {sum_ages / len(students)}')
