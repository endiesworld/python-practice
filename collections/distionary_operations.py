#  Dictionary operations in Python  visit https://docs.python.org/3/library/stdtypes.html#mapping-types-dict for more methods

my_details = {
    'firstname': 'Emmanuel',
    'surname': 'Okoro',
}

age = input('Enter your age: ')

# To add new attribute(key: value) to a python dictionary
my_details['age'] = age

height = input('Enter your height in feet: ')

my_details['height'] = height

print('Hello there, I am {} years old and I am {} feet tall'.format(
    my_details['age'], my_details['height']))

my_wife = {
    'wife_name': 'Adaobi',
    'surname': 'Okoro'
}

# Update the dictionary keys and values, with another keys and values
my_details.update(my_wife)

print('My details are: ', my_details)
