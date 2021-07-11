letters_counter = lambda lst : [len(x) for x in lst]

animal_list=['cat','fish','elephant']
print(letters_counter(animal_list))

sum = lambda a,b : a + b
sub = lambda a,b : a - b
print(sum(5,10))
print(sub(10,5))

calculator = {
    'sum': lambda a,b : a + b,
    'sub': lambda a,b : a - b,
    'mul': lambda a,b : a * b,
    'quot': lambda a,b : a/b
}

print(type(calculator))

sum = calculator['sum']
mul = calculator['mul']
print('The sum is: {}'.format(sum(10,5)))
print('The multiplication: {}'.format(mul(10,5)))