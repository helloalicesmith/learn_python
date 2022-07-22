def foo(required, *args, **kwargs):
    print(required, args, kwargs)

foo('hi', 1, 2, 3)
foo('hi', 1, 2, 3, key1='key', key2='key2')

# * = кортеж
# ** = словарь

class A:
    def __init__(self, *args, **kwargs):
        print(args, kwargs)


class B(A):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

b = B(1, 2, key='value')

def baz(x, y, z):
    print(f'--> {x} {y} {z} <--')

tuple_var = (1,2,3)
dict_var = { 'x': 0, 'y': 4, 'z': 5 }

baz(tuple_var[0], tuple_var[1], tuple_var[2])
baz(*tuple_var)

baz(**dict_var)
