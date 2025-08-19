# def list_subset(n):
#     result = []
    
#     def backtracking(sub_list, ptr):
        
            
#         result.append(sub_list[:])
        
#         for li in range(ptr, len(n)):
#             sub_list.append(n[li])
#             backtracking(sub_list,  ptr + 1)
#             sub_list.pop()
            
    # return result
    
def list_subset(arr):
    result = []
    sub_set = []
    arr_len = len(arr)
    ptr = 0
    def backtracking(ptr, sub_set):
        if ptr == arr_len:
            result.append(list(sub_set))
            return
            
        sub_set.append(arr[ptr])
        
        backtracking(ptr +1, sub_set)
        sub_set.pop()
        backtracking(ptr+1, sub_set)
        
        
    backtracking(ptr, sub_set)
    return result

if __name__ == "__main__":
    n = [1, 2, 3]
    print("Generating all subsets of the list:", n)
    
    combinations = list_subset(n)
    print("All combinations of subsets:", combinations)