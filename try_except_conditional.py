def convert_number(value):
    try:
        value = int(value)
        return value
    except ValueError:
        try:
            value = float(value)
            return value
        except ValueError:
            pass

while True:
    number = convert_number(input('Number: '))

    if number is None:
        print('Error: its not a number')
    else:
        print(number * 2)