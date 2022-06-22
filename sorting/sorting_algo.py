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
    until size is 1.
"""


def merge_sort(list):
    list_len = len(list)
    print(f'Caller list: {list}')
    if list_len == 1:
        return list[0]

    mid = list_len // 2
    left_list = list[:mid]
    right_list = list[mid:]

    left_side = merge_sort(left_list)
    print(f'left list is: {left_side}')
    right_side = merge_sort(right_list)

    return [left_side, right_side]


items = [1, -3, 2, 0, 3, -2, -1]

print(merge_sort(items))
