"""
    iterable: Can be passed to iter() to produce an iterator.
    iterator: Can be passed to next() to get the next value in the sequence.
"""


def next_value(iterable):
    try:
        return next(iterable)
    except StopIteration:
        raise ValueError('End of sequence reached')


def iterator_func(sequence):
    return iter(sequence)


caller = iterator_func([2, 4, 6, 8])
print(next(caller))
print(next(caller))
# # def iterator_func(sequence):
# #     iterable = iter(sequence)
# #     try:
# #         return next(iterable)
# #     except StopIteration:
# #         # return 'End of sequence reached'
# #         raise ValueError('End of sequence reached')


# list_collection = [2, 4, 6, 8]
# set_collection = {2, 4, 6, 8}
# list_iterable = iter(list_collection)
# set_iterable = iter(set_collection)


# def get_next_list_val():
#     global list_iterable
#     try:
#         return next(list_iterable)
#     except StopIteration:
#         # return 'End of sequence reached'
#         raise ValueError('End of sequence reached')


# print(get_next_list_val())
# print(get_next_list_val())
# print(get_next_list_val())
# print(get_next_list_val())
# print(get_next_list_val())
# for position, value in enumerate(list_collection):
#     print(
#         f'Element value in position {position + 1 } in the list sequence: {iterator_func(list_collection)}')

#     print(
#         f'Element value in position {position + 1 } in the list sequence: {iterator_func(set_collection)}')
