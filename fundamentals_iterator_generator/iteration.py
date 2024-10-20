"""
Iterable:
    An iterable is any Python object that can return its elements one at a time, allowing you to iterate over them in a loop (like a for loop).
    In Python, an object is considered an iterable if it has a method called __iter__(), which returns an iterator.
    
Iterator:
    An iterator is an object that keeps state of where it is during iteration. It knows how to get the next item in the sequence, 
    one at a time, until it raises a StopIteration exception, signaling that the sequence is done.

    An iterator has two main methods:
    __iter__() — This returns the iterator object itself.
    __next__() — This returns the next item in the sequence. When there are no more items, it raises the StopIteration exception.
    
    Key Points to Remember:
    All iterators are iterables, but not all iterables are iterators.
    To get an iterator from an iterable, you use iter().
    You can manually iterate through an iterator using next()

    iterable: Can be passed to iter() to produce an iterator.
    iterator: Can be passed to next() to get the next value in the sequence.
    
Some Common Confusions (Hubris):
    Is a list an iterator? No. A list is an iterable, but it’s not an iterator itself. You need to convert it into an iterator using iter().

    Can you reset an iterator? No. Once an iterator is exhausted (you've looped through it or called next() until StopIteration), 
    it cannot be reset. You would need to create a new iterator from the iterable.

    Why doesn't calling __next__() on an iterable work? Because iterables don’t have a __next__() method. Only iterators have it. 
    You first need to get an iterator from an iterable (using iter()) and then call next().

"""


def iterator_func(sequence):
    iterable = iter(sequence) # Here we convert all iterables to an iterator

    def next_value():
        try:
            return next(iterable) 
        except StopIteration:
            raise ValueError('End of sequence reached')

    return next_value


list_collection = [2, 4, 6, 8] # here list_collection is an iterable because it assigned to it is a list, and list is an iterable
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

my_string = "emmanuel"
my_string_iterator = iter(my_string)
print(*my_string_iterator) # * unpacks the content of an iterator, with no element remaining