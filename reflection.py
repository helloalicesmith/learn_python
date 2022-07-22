class ClassA:
    name: str

class ClassB:
    name: str

g = globals().copy()
for name, obj in g:
    print(name, obj)
