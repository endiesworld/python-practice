def list_subset(n):
    result = []
    
    def backtracking(sub_list, ptr):
        
            
        result.append(sub_list[:])
        
        for li in range(ptr, len(n)):
            sub_list.append(n[li])
            backtracking(sub_list,  ptr + 1)
            sub_list.pop()
            
        
            
    return result