from string import Template

name = 'Alice'
second_name = 'Smith'
i = 404

# 1. printf as C
print('hello %s' % name)
print('hello %s %s!' % (name, second_name))
print('hello %(name)s, hello %(name)s %(second_name)s!\n' % { "name": name, "second_name": second_name })

# 2. python 2.7
print('hello {}'.format(name))
print('hello {name} {second}'.format(second=second_name, name=name))
print('int {i:x}\n'.format(i=i)) # format spec

# 3. python 3.6
print(f'hello {name}!')
print(f'2 * (3 + 5) = {2 * (3 + 5)}')
print(f'int {i:x}')

# 4. template
t = Template('hello, $name!')
print(t.substitute(name=name))

secret = 'my_secret'

class Error:
    def __init__(self):
        pass

err = Error()
user_input = '${error.__init__.__globals__[secret]}'
user_input2 = '${error}'

print(Template(user_input).substitute(error=err))
