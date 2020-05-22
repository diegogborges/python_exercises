try:
    print(a)
except NameError as erro:
    print('Developer error, talk to him.')

try:
    a = []
    print(a[1])
except IndexError as erro:
    print('Index error.')

try:
    print(a)
except Exception as erro:
    print('Unexpected error')

try:
    print(a)
    a = []
    print(a[1])
except NameError as erro:
    print('Developer error, talk to him.')
except IndexError as erro:
    print('Index error.')
except Exception as erro:
    print('Unexpected error')

try:
    print(a)
    a = []
except NameError as erro:
    print('Developer error, talk to him.')
except IndexError as erro:
    print('Index error.')
except Exception as erro:
    print('Unexpected error')
else:
    print('Code successfully executed')
finally:
    print('Always runs at the end')

print('continue')
