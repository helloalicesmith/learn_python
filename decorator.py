def tag_wrapper(tag):
    def close_tag(tag):
        # TODO closing tag
        return tag

    def decorator(func):
        def wrapper(*args, **kwargs):
            return tag + func(*args, **kwargs) + close_tag(tag)
        return wrapper

    return decorator 

@tag_wrapper('<h1>')
def say(x):
    return x

result = say('hello')

print(result)
