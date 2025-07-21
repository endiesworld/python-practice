"""Level 1: Build All Binary Strings of Length N
Input: n = 2

Output: ['00', '01', '10', '11']

VISUALIZATION(n=2):
            ""
          /    \
        0        1
       / \      / \
     00  01   10  11


"""


def binary_string_builder(n):
    binary = ''
    zero = '0'
    one = '1'
    binary_list = []
    
    def binary_builder(binary):
        if len(binary) == n :
            binary_list.append(binary)
            return
            
        if len(binary) < n :
            current = binary
            binary += zero
            binary_builder(binary)
            binary = current
            
        if len(binary) < n:
            binary += one
            binary_builder(binary)
            
    binary_builder(binary)
    return binary_list
    
    
if __name__ == "__main__":
    n = 3
    print("Generating parentheses for n =", n)
    
    print(binary_string_builder(n))