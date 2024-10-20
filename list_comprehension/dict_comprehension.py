"""
Dict comprehensions
    Now we can also write dictionary comprehensions to create new dictionaries from iterables. 
    The syntax is almost the same as in list comprehensions and there are 2 differences. One, we use curly braces instead of square brackets. 
    Two, the key and value are separated by a colon in the output expression as we can see here. In this example,
    we are creating a dictionary with keys positive integers and corresponding values the respective negative integers.    
    
"""

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}

# Print the new dictionary
print(new_fellowship)