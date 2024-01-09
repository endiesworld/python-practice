import copy

def print_subset(arr, length, index, store):
    if index == length:
        print(store)
        return
    
    print_subset(arr, length, index+1, store)
    # store = store + [arr[index]]
    store.append(arr[index])
    # st = copy.deepcopy(store)
    print_subset(arr, length, index+1, store)
    store.pop()
    return


print_subset([1,2,3], 3, 0, [])