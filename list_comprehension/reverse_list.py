


"""
# Understanding Variable Assignment in Python vs. Java/C++
#Python (Pass-by-Object-Reference)
    In Python, everything is an object, and variables are references (pointers) to objects in memory.
    When you pass a list to a function, you pass a reference to the original object, but reassigning the reference inside the function does not affect the caller’s list.

#C++ and Java (Pass-by-Value and Reference Differences)
    In C++, when you pass an array (or a reference), modifying it inside a function affects the original.
    In Java, arrays are passed as references, similar to Python, but assignment (arr = newArray) behaves differently because Java variables are more like pointers.
"""
def reverse(arr: list):
    arr_len = len(arr)
    temp_list = []
    for i in range(arr_len):
        temp_list.append(arr[arr_len -1 - i])
    print("Array: ", temp_list)
    arr = temp_list
    

# THE OPERATION YOU DESIRE IS
def reverse_in_place(arr):
    arr[:] = arr[::-1]  # This modifies the original list, rather than reassigning arr

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    print("List before reverse: ", nums)
    reverse(nums)
    print("List after an attemped reverse: ", nums)
    reverse_in_place(nums)
    print("List after reverse: ", nums)