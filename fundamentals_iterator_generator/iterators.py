"""
    Using enumerate():
        enumerate is a function that takes any iterable as argument, such as a list, and returns a special enumerate object, 
        which consists of pairs containing the elements of the original iterable, along with their index within the iterable. 
        We can use the function list to turn this enumerate object into a list of tuples and print it to see what it contains. 
        The enumerate object itself
"""

avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
e = enumerate(avengers)
print(type(e))
print(list(e))

for index, value in e:
    print(f"index: {index}", f"value: {value}")
    
    

"""
    Using zip()
        Now let's move on to zip, which accepts an arbitrary number of iterables and returns an iterator of tuples. 
        Here we have two lists, one of the avengers, the other of their names. Zipping them together creates a zip object which is an 
        iterator of tuples. We can turn this zip object into a list and print the list. The first element is a tuple containing the first 
        elements of each list that was zipped. The second element is a tuple containing the second elements of each list that was zipped and so on.    
    
"""

names = ['barton', 'stark', 'odinson', 'maximoff']

z = zip(avengers, names)
print(type(z))

z_list = list(z)
print(list(z_list))

for data_a, data_b in z:
    print(data_a, data_b)