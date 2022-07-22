import functools

def close_tag(tag):
    # TODO closing tag
    return tag

def tag_wrapper(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """add html tag"""
            return tag + func(*args, **kwargs) + close_tag(tag)
        return wrapper

    return decorator 

@tag_wrapper('<div>')
@tag_wrapper('<h1>')
def say(x):
    """say something"""
    return x

result = say('hello')

print(f'doc: {say.__doc__}, name: {say.__name__}')
print(result)
