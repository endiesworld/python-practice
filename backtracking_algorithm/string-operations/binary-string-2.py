"""
    Level 2 Challenge:
    Generate all binary strings of length n such that there are no two consecutive 1s.
    
    Input: n = 3

    Output: ['000', '001', '010', '100', '101']
    
"""

def binary_string(n):
    current_string = ""
    zero = '0'
    one = '1'
    result = []
    
    def backtracking(current_string):
        if len(current_string) == n:
            result.append(current_string)
            return
            
        state = current_string
        
        if len(current_string) < n:
            current_string += zero
            backtracking(current_string)
            
        current_string = state
        
        if (len(current_string) > 0 ) and (current_string[-1] == one):
            return 
            
        if len(current_string) < n:
            current_string += one
            backtracking(current_string)
    
    backtracking(current_string)
    return result

if __name__ == "__main__":
    n = 3
    print("Generating binary strings of length n =", n)
    
    combinations = binary_string(n)
    print("All combinations of binary strings:", combinations)