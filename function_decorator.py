from time import time


def velocity(function):
    def intern(*args, **kwargs):
        start_time = time()
        function(*args, **kwargs)
        end_time = time()
        final_time = (end_time - start_time) * 1000
        print(f'\nFunction {function.__name__}() spended {final_time:.2f}ms to execute.')
        return function(*args, **kwargs)

    return intern


@velocity
def lag():
    for i in range(10000):
        print(i, end='')


lag()
