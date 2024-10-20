"""
    List comprehensions
        list comprehensions collapse for loops for building lists into a single line and the required components are:
        1) an iterable, 
        2) an iterator variable that represents the members of the iterable and 
        3) an output expression. That's it. You can also use list comprehensions in place of nested for loops.    
    labels = [EXPRESSION for char in my_string]
"""

#  List comprehensions are a compact way to create lists in Python and can sometimes be more efficient
# (i.e. execute faster) than generic for loops in Python
# [ return computation on this item for item in list if item satisfies condition ]

nums = [1, 2, 3, 4, 5, 6]

even_squared = [x**2 for x in nums if x % 2 == 0]

print(f' Even numbers squared is: ', even_squared)

list_a = [1, 2, 3, 4, 6, 7, 9, 11]
list_b = [2, 3, 4, 5, 11]

intersection = [a for a in list_a for b in list_b if a == b]

print(intersection)

my_string = 'explore'
vowels = 'aeiou'
labels = ['vowel' if char in vowels else 'consonant' for char in my_string]
# [expression for statement]
print(labels)

a = [1, 2, 3]
b = [4, 5, 6]

# where i is an item in list a, and j is an item in list b
c = [i+j for i, j in zip(a, b)]
print(f'C : ', c)  # [5, 7, 9]

x = [1, 2, 3, 4, 5, 6, 7]
y = ['a', 'b', 'c']
z = [x for x in zip(x, y)]
print('z : ', z)  # [(1, 'a'), (2, 'b'), (3, 'c')]

result = []
RESPONSE_REQUIRED = [['when', 'how', 'what', 'who', 'can', 'know'], [
    'when', 'how', 'what', 'who', 'can', 'know'], ['when', 'how', 'what', 'who', 'can', 'know']]
for data in RESPONSE_REQUIRED:
    r = ' '.join(d for d in data)
    result.append(r)

print(result)

# Nested list comprehension
# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0,5)]  for row in range(0,5)]

print(matrix)

# Print the matrix
for row in matrix:
    print(row)