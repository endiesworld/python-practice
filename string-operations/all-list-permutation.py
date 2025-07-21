# def permuation(n):
#     result = []
    
    

#     def backtracking(current_perm, ptr):
#         if current_perm[0] == n[ptr]:
#             result.append(current_perm)
#             return
            
#         for indx in range(ptr, len(n)):
#             current_perm.append(n[indx])
#             backtracking(current_perm, ptr + 1)
#             current_perm.pop()
            
#     backtracking(n, 0)
#     return result

def generate_permutations(nums):
    result = []

    def backtrack(current_perm):
        if len(current_perm) == len(nums):
            result.append(current_perm[:])  # Save a copy
            return

        for num in nums:
            if num in current_perm:
                continue  # Skip already used numbers
            current_perm.append(num)
            backtrack(current_perm)
            current_perm.pop()

    backtrack([])
    return result

if __name__ == "__main__":
    n = [1, 2, 3]
    print("Generating all permutations of the list:", n)
    
    combinations = generate_permutations(n)
    print("All combinations of permutations:", combinations)
    
  