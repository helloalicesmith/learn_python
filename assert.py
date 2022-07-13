obj = {
    "a": 10,
    "b": 5,
}

def some_func():
    x = obj['a'] - obj['b']
    assert 0 < x < 12
    return x

# Disable assertions: python -O assert.py 
print(some_func())
