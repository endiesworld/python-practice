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

card = [13, 11, 10, 7, 4, 3, 1, 0, -3, -7, - 9]
number = 3

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


# def loop_binary_search(list, element):
#     arr_size = len(list)
#     if arr_size == 1:
#         return 0 if list[0] == element else None

#     index = None
#     start = 0
#     stop = arr_size

#     while start < stop:
#         mid_point = (start + stop) // 2
#         print('mid point is: {}, start point is: {}, stop point is: {}'.format(
#             mid_point, start, stop))
#         if list[mid_point] == element:
#             index = mid_point
#             break
#         if mid_point == start:
#             break
#         elif list[mid_point] > element:
#             start = mid_point
#         else:
#             stop = mid_point
#     return index


# def search(nums, target: int) -> int:

#     arr_size = len(nums)

#     if nums[0] == target:
#         return 0

#     index = -1
#     start = 0
#     stop = arr_size

#     while start < stop:
#         mid_point = (start + stop) // 2
#         if nums[mid_point] == target:
#             index = mid_point
#             break
#         elif (stop == mid_point) | (start == mid_point):
#             break
#         elif nums[mid_point] > target:
#             stop = mid_point
#         else:
#             start = mid_point
#     return index


def search(nums, target):
    right = len(nums) - 1
    return search_(nums, target, 0, right)


def search_(nums, target, left, right):
    if (left > right):
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        right = mid - 1
        return search_(nums, target, left, right)
    elif nums[mid] < target:
        left = mid + 1
        return search_(nums, target, left, right)


# print(recursive_binary_seach(card, number))
# print(loop_binary_search(card, number))
print(search([-2, -1, 0, 2, 3, 5, 9, 12], -2))
