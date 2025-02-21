

def merge(arr, i, j, k):
    left_start = i
    right_start = j + 1
    
    sorted_arr = []
    
    while( left_start <= j and right_start <= k ):
        if(arr[left_start] <= arr[right_start]):
            sorted_arr.append(arr[left_start])
            left_start += 1
            
        else:
            sorted_arr.append(arr[right_start])
            right_start += 1
            
            
    while(left_start <= j):
        sorted_arr.append(arr[left_start])
        left_start += 1
        
        
    while(right_start <= k-1):
        sorted_arr.append(arr[right_start])
        right_start += 1
        
    
    for indx in range(len(sorted_arr)):
        arr[i + indx] = sorted_arr[indx]
    

def helper_sort_asc(arr, i, k):
    j = (i + k) // 2
    
    print(f"LEFT SIDE: (i: {i}, j: {j}), RIGHT SIDE: (j: {j+1}, k: {k})")

    
    if( i < k):
        helper_sort_asc(arr, i, j)
        helper_sort_asc(arr, j+1, k)
        merge(arr, i, j, k)


def sort_asc(arr):
    i = 0
    k = len(arr) - 1
    
    helper_sort_asc(arr, i, k)
    
    
if __name__ == '__main__':
    arr = [45, 67, 8,10 , 8, 5, 20, 58, 6, 10, 5, 14]
    print(sort_asc(arr) )
    print("Sorted array: ", arr)