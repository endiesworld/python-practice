# Lambda Function

from tkinter import Y


def my_lambda(x): return x * x


print(my_lambda(5))  # 25

# Mapping, a built in python function map(func, iterable)
# Mapping returns an iterator that applies function to every element in the iterable

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 10]

# The lambda function acts like a JavaScript callback function
my_list_sqr = list(map(my_lambda, my_list))

print('my_list_sqr is now: ', my_list_sqr)

# Filtering Construct an iterator from those elements of iterable for which function returns true.
even_numbers = list(filter(lambda x: (x % 2) == 0, my_list))

print('The even numvers in the list are: ', even_numbers)
