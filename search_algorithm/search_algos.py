# Linear Search O(n)
"""
    Linear search is a very basic and simple search algorithm. In Linear search, 
    we search an element or value in a given array by traversing the array from the starting, 
    till the desired element or value is found.
    It is used for unsorted and unordered small list of elements.
"""

# Binary Search O(logn)
"""
    Binary Search is used with sorted array or list. In binary search, we follow the following steps:

    We start by comparing the element to be searched with the element in the middle of the list/array.
    If we get a match, we return the index of the middle element.

    If we do not get a match, we check whether the element to be searched is less or greater than in value than the middle element.

    If the element/number to be searched is greater in value than the middle number, 
    then we pick the elements on the right side of the middle element(as the list/array is sorted, hence on the right, 
    we will have all the numbers greater than the middle number), and start again from the step 1.

    If the element/number to be searched is lesser in value than the middle number, 
    then we pick the elements on the left side of the middle element, and start again from the step 1.

    Binary Search is useful when there are large number of elements in an array and they are sorted.
"""

# QUESTION 1:
"""
    Alice has some cards with numbers written on them. She arranges the cards in decreasing order, 
    and lays them out face down in a sequence on a table. 
    She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. 
    Write a function to help Bob locate the card.

    Card = [13, 11, 10, 7, 4, 3, 1, 0] 
    number: 7
"""


from unittest import result
card = [13, 11, 10, 7, 4, 3, 1, 0, -3, -7, - 9]
number = 14


def search_func(card, number):

    card_len = len(card)
    # print("Length of card is: ", card_len)
    return search_func_(card, number, left=0, right=card_len)


def search_func_(card, number, left, right):
    if (left >= right):
        return None
    mid = (left + right) // 2

    result = card[mid]

    if result == number:
        return mid
    elif number < result:
        # print(f'left remain, right changed to {mid}')
        return search_func_(card, number, left, mid)

    elif number > result :
        # print(f'right changed to {mid}')
        return search_func_(card, number, mid + 1, right)
    
    return "Value not in list"

# print(search_func(card, number))


# Recursive solution for binary search for list sorted in descending order


# def recursive_binary_seach(list, element, start=False, stop=False):
#     arr_size = len(list)
#     start = start
#     stop = stop
#     if arr_size == 1:
#         return 0 if list[0] == element else None

#     if not start:
#         start = 0

#     if not stop:
#         stop = arr_size

#     if (list[start] < element) | (list[stop - 1] > element):
#         return None
#     mid_index = (start + stop) // 2
#     print('mid point is: {}, start point is: {}, stop point is: {}'.format(
#         mid_index, start, stop))
#     if list[mid_index] == element:
#         return mid_index

#     elif list[mid_index] < element:
#         stop = mid_index
#         return recursive_binary_seach(list, element, start=start, stop=stop)
#     else:
#         start = mid_index
#         return recursive_binary_seach(list, element, start=start, stop=stop)




# def search(nums, target):
#     right = len(nums) - 1
#     return search_(nums, target, 0, right)


# def search_(nums, target, left, right):
#     if (left > right):
#         return -1

#     mid = (left + right) // 2

#     if nums[mid] == target:
#         return mid
#     elif nums[mid] > target:
#         right = mid - 1
#         return search_(nums, target, left, right)
#     elif nums[mid] < target:
#         left = mid + 1
#         return search_(nums, target, left, right)


# # print(recursive_binary_seach(card, number))
# # print(loop_binary_search(card, number))
print(search_func([-2, -1, 0, 2, 3, 5, 9, 12], -2))
print(search_func([5,6,7,8,9], 9))
print(search_func([5,6,7,8,9], 10))
print(search_func([5,6,7,8,9], 8))
print(search_func([5,6,7,8,9], 4))
print(search_func([5,6,7,8,9], 6))



