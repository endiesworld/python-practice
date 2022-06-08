

# List operations for more methods, visit https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

my_details = ['Emmanuel', 'Okoro']

my_details.append(35)
my_details.append('Adaobi')

print('The length of the list is: ', len(my_details))
print('The elements are: ', my_details)

# Inserting elements
first_name = input('Enter your firstname: ')
my_details.insert(0, first_name)

print('The length of the list is: ', len(my_details))
print('The elements are: ', my_details)

print("*********** SLICING FROM ELEMENT 2 - 4 *******************")
print(my_details[2:4])
