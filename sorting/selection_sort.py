from typing import List

def selection_sort(nums: List) -> List:
    for index, data in enumerate(nums):
        max = data
        for next_index, next_data in enumerate(nums[1+index:]):
            if next_data < max:
                nums[index] = next_data
                nums[next_index + index + 1] = max
                max = next_data
    return 


def partial_selection_sort_rec(arr):
    arr_len = len(arr)
    for i in range(len(arr)):
        
        def selection_sort_rec_(arr, arr_len, cur_index, shift):
            if arr_len <= cur_index + shift:
                return
            next_index = cur_index + shift
            cur_index_element = arr[cur_index]
            next_data = arr[next_index]
            if cur_index_element < next_data :
                arr[cur_index] = next_data
                arr[next_index]  = cur_index_element 
            shift += 1
            selection_sort_rec_(arr, arr_len, cur_index, shift)
        selection_sort_rec_(arr, arr_len, i, 1)


def selection_sort_recus(arr):
    def selection_sort_recus_(arr, arr_len, start, next):
        if arr_len == start :
            return
        start += 1
        next = 1
        def selection_sort_rec_(arr, arr_len, cur_index, shift):
            if arr_len <= cur_index + shift:
                return
            next_index = cur_index + shift
            cur_index_element = arr[cur_index]
            next_data = arr[next_index]
            if cur_index_element < next_data :
                arr[cur_index] = next_data
                arr[next_index]  = cur_index_element 
            shift += 1
            selection_sort_rec_(arr, arr_len, cur_index, shift)
        selection_sort_rec_(arr, arr_len, start, next)
        
        selection_sort_recus_(arr, arr_len, start, next)
    
    arr_len = len(arr)
    start = -1
    next = 1
    selection_sort_recus_(arr, arr_len, start, next)



data = [3,4,5,2,1, 10, 6, 9 ,23]
# selection_sort(data)
# partial_selection_sort_rec(data)
selection_sort_recus(data)
print(data)