from dados import products, students, my_list

new_list = map(lambda x: x * 2, my_list)
print()
print(list(new_list))

new_list = [x * 2 for x in my_list]
print()
print(list(new_list))

for product in products:
    print(product)

pricies = map(lambda p: p['price'], products)

for price in pricies:
    print(price)


def increments_price(p):
    p['price'] = round(p['price'] * 1.05, 2)
    return p

new_products = map(increments_price, products)

for product in new_products:
    print(product)


ages = map(lambda p: p['age'] * 1.20, students)

for age in ages:
    print(age)



def increments_age(p):
    p['new_age'] = round(p['age'] *  1.20)
    return p

ages = map(increments_age, students)

for age in ages:
    print(age)