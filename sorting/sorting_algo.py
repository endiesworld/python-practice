# Bubble Sort
"""
    Each bubble up takes a full sweep through the list, swapping the adjacent elements, if they are in
    the wrong order. The complexity for Bubble sort is O(n^2)
"""

# Insertionv Sort
"""
    The array is split into a sorted and unsorted part, values from the unsorted part are picked and 
    placed at the correct position in the sorted part. The complexity is O(n^2)
"""

# Merge Sort
"""
    Works by subdividing the list into two sub-lists, sorting them using merge sort and 
    then merging them back up. Recursive call is made to subdivide eachv list into sublist
    until size is 1. The complexity is O(nlogn)
"""


def merge(list_1, list_2):
    container = []
    len_1 = len(list_1)
    len_2 = len(list_2)
    count_1 = 0
    count_2 = 0

    while (count_1 < len_1) & (count_2 < len_2):
        if list_1[count_1] < list_2[count_2]:
            container.append(list_1[count_1])
            count_1 += 1
        else:
            container.append(list_2[count_2])
            count_2 += 1

    container = container + list_1[count_1:]
    container = container + list_2[count_2:]

    return container


def merge_sort(list):
    list_len = len(list)
    if list_len == 1:
        return list

    mid = list_len // 2
    left_list = list[:mid]
    right_list = list[mid:]

    left_side = merge_sort(left_list)
    right_side = merge_sort(right_list)

    sorted = merge(left_side, right_side)
    return sorted


items = [1, -3, 2, 0, 3, -2, -1]

print(merge_sort(items))
