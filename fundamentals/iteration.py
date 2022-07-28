"""
    iterable: Can be passed to iter() to produce an iterator.
    iterator: Can be passed to next() to get the next value in the sequence.
"""


def iterator_func(sequence):
    iterable = iter(sequence)

    def next_value():
        try:
            return next(iterable)
        except StopIteration:
            raise ValueError('End of sequence reached')

    return next_value


list_collection = [2, 4, 6, 8]
set_collection = {2, 4, 6, 8}
list_caller = iterator_func(list_collection)
set_caller = iterator_func(set_collection)

print(list_caller())
print(list_caller())
print(list_caller())
print(list_caller())
print('================= SET_CALLER =============')
print(set_caller())
print(set_caller())
print(set_caller())
print(set_caller())
