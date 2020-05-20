from dados import products, students, my_list

nova_lista = filter(lambda x: x > 5, my_list)
print(list(nova_lista))

#list comparations
nova_lista = [x for x in my_list if x > 5]
print(list(nova_lista))

nova_lista = filter(lambda p: p['price'] > 50, products)
for product in nova_lista:
    print(product)

print()
def filter_students(student):
    if student['age'] < 18:
        return True

nova_lista = filter(filter_students, students)
for student in nova_lista:
    print(student)