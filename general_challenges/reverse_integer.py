def reverse(x: int) -> int:
        mini = -2**31
        maxi = (2**31 - 1)
        bias = 1 
        if x < 0:
            bias = -1
            x = x * bias
        
        x = str(x)
        x = x[::-1]
        # len_x = len(x)
        # negative_index = -1
        # while abs(negative_index) <= len_x:
        #     store += x[negative_index]
        #     negative_index -= 1
        store = int(x)
        store = store * bias
        if (store < mini) or (store > maxi):
            return 0
        return store 
    
    
x = 123
x = -123
# x = 120
print(reverse(x))