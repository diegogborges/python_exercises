def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('Log: ', error)
        raise

try:
    print(divide(2,0))
except ZeroDivisionError as error:
    print(error)

print()

# with raise
def divide_raise(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('Log: ', error)
        raise

try:
    print(divide_raise(2,0))
except ZeroDivisionError as error:
    print(error)


# with raise
def divide_r(n1, n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser 0.")
    return n1 / n2

try:
    print(divide_raise(2,0))
except ZeroDivisionError as error:
    print(error)