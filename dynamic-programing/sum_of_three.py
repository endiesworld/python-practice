
parent_store = []

def print_subset(arr, length, index, store):
    if index == length:
        return
    if len(store) == 3 and sum(store) == 0:
        if parent_store :
            post = False
            for arr_ in parent_store:
                print("checked:", store)
                if not (arr_[0] in store and arr_[1] in store and arr_[2] in store):
                    post = True
            if post:
                parent_store.append(store[:])
        else:
            parent_store.append(store[:])
    print_subset(arr, length, index+1, store)
    # store = store + [arr[index]]
    store.append(arr[index])
    # st = copy.deepcopy(store)
    print_subset(arr, length, index+1, store)
    store.pop()
    return


print_subset([-1,0,1,2,-1,-4], 6, 0, [])
print(parent_store)