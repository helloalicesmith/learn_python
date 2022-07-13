from contextlib import contextmanager
# TODO

with open('hello.txt', 'w') as f:
    f.write('hello world!')

file = open('some_file', 'w')
try:
    file.write('Hola!')
finally:
    file.close()

# context managers for "with"
# __enter__ && __exit__

class ManagerHello:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f'hello {self.name} from __enter__ !')

    def __exit__(self, exit_type, exit_val, ext_tb):
        print(f'hello {self.name} from __exit__ !')

with ManagerHello('LoL') as f:
    pass

class ManagerFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')

    def __exit__(self, exit_type, exit_val, ext_tb):
        if self.file:
            self.file.close()

class Indenter:
    def __init__(self):
        self.count = 0

    def __enter__(self):
        self.count += 1

    def __exit__(self, exit_type, exit_val, ext_tb):
        self.count -= 1

    def print(self, value):
        print(' ' * self.count + value)

with Indenter() as indent:
    pass
