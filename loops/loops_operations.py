#  Loops operations

# prints x value from 0 - 9
# range is an iterable python function, it can also have a start value, stop value and step
for x in range(5):
    print(f'The current value of x is: {x}')


# Iterating through a list
tenants = ['Emmanuel', 'Lawrence', 'Rober']
for tenant in tenants:
    print(f'{tenant} is a tenant for house 15')

# To access both index and list value, use the enumerate function
tenants = ['Emmanuel', 'Lawrence', 'Rober']
for index, tenant in enumerate(tenants):
    print(f'{tenant} is a tenant number {index}, for house 15')

# Iterate through a dictionary.
my_details = {
    'firstname': 'Emmanuel',
    'lastname': 'Okoro',
    'age': 35,
    'heigth_ft': 5.11
}
# Return items in the dictionary as a key value tuple (key, value)
# To access keys or values separately, we do: dict.keys() or dict.values()
for detail in my_details.items():
    print('{}'.format(detail))
