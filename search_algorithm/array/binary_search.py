# Binary Search O(logn)
"""
    Binary Search is used with sorted array or list. In binary search, we follow the following steps:

    We start by comparing the element to be searched with the element in the middle of the list/array.
    If we get a match, we return the index of the middle element.

    If we do not get a match, we check whether the element to be searched is less or greater than in value than the middle element.

    If the element/number to be searched is greater in value than the middle number, 
    then we pick the elements on the right side of the middle element(as the list/array is sorted, hence on the right, 
    we will have all the numbers greater than the middle number), and start again from the step 1.

    If the element/number to be searched is lesser in value than the middle number, 
    then we pick the elements on the left side of the middle element, and start again from the step 1.

    Binary Search is useful when there are large number of elements in an array and they are sorted.
"""

# QUESTION 1:
"""
    Alice has some cards with numbers written on them. She arranges the cards in decreasing order, 
    and lays them out face down in a sequence on a table. 
    She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. 
    Write a function to help Bob locate the card.

    Card = [13, 11, 10, 7, 4, 3, 1, 0] 
    number: 7
"""

def search_recus(arr, element, start, end):
    if(start > end): return None
    
    mid = (start + end) // 2
    
    result =  arr[mid]
    
    if(result == element): return mid
    
    if(result > element):
        start = mid + 1
        return search_recus(arr, element, start, end)
    else:
        end = mid - 1
        return search_recus(arr, element, start, end)

def search_fn(arr, element):
    start = 0
    end = len(arr) -1
    mid = end // 2
    
    result = arr[mid]
    
    if(result == element):
        return mid
    
    # THE ORDER OF THE ARRAY DETERMINES the end and the start
    if (result > element):
        start = mid + 1
        return search_recus(arr, element, start, end)
    else:
        end = mid - 1
        return search_recus(arr, element, start, end)
    

    
def search_non_recusive(arr, element):
    
    start = 0
    end = len(arr) - 1
    mid = end // 2
    
    while (start < end):
        result = arr[mid]
        
        if(result == element):
            return mid
        elif( result > element ):
            start = mid + 1
            mid = (start + end) // 2
        else:
            end = mid - 1
            mid = (start + end) // 2
            
    return None



if __name__ == '__main__':
    # print(search_fn([13, 11, 10, 7, 4, 3, 1, 0, -5, -9, -20], -9))
    # print(search_fn([13, 11, 10, 7, 4, 3, 1, 0], 7))
    # print(search_fn([13, 11, 10, 7, 4, 3, 1, 0, -5, -9, -20], -30))
    # print(search_fn([13, 11, 10, 7, 4, 3, 1, 0, -5, -9, -20], 15))
    
    print(search_non_recusive([13, 11, 10, 7, 4, 3, 1, 0, -5, -9, -20], -9))
    print(search_non_recusive([13, 11, 10, 7, 4, 3, 1, 0], 7))
    print(search_non_recusive([13, 11, 10, 7, 4, 3, 1, 0, -5, -9, -20], -30))
    print(search_non_recusive([13, 11, 10, 7, 4, 3, 1, 0, -5, -9, -20], 15))