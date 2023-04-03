from typing import List



def merge_two_sorted_arrays(arr1 :List, arr2 :List) -> List:
    combine_arr = []
    index_pos_1 = 0
    index_pos_2 = 0
    len_1 = len(arr1)
    len_2 = len(arr2)
    while((index_pos_1 < len_1) and (index_pos_2 < len_2)):
        if (arr1[index_pos_1] <= arr2[index_pos_2]):
            combine_arr.append(arr1[index_pos_1])
            index_pos_1 += 1
        else:
            combine_arr.append(arr2[index_pos_2])
            index_pos_2 += 1
    while (index_pos_1 < len_1) :
        combine_arr.append(arr1[index_pos_1])
        index_pos_1 += 1
    while (index_pos_2 < len_2):
        combine_arr.append(arr2[index_pos_2])
        index_pos_2 += 1
    
    return combine_arr

def merge_sort(arr: List) -> List:
    arr_len = len(arr)
    if arr_len == 1:
        return arr

    mid = int(arr_len / 2)
    right_arr = arr[mid:]
    left_arr = arr[:mid]
    sorted_right_arr = merge_sort(right_arr)
    sorted_left_arr = merge_sort(left_arr)
    
    return merge_two_sorted_arrays(sorted_right_arr, sorted_left_arr)

# arr_1 = [5,8,12,56]
# arr_2 = [7,9,45,51]

arr = [45, 67, 8,10 , 8,5, 20, 58, 6, 10, 5, 14]
print(merge_sort(arr) )