def sum_set_(arr, val, index):
    if val == 0:
        return 1
    elif val < 1:
        return 0
    elif index < 0:
        return 0
    elif arr[index] > val:
        return sum_set_(arr, val, index-1)
    else:
        return sum_set_(arr, (val - arr[index]), index-1) + sum_set_(arr, val, index-1) 



def sum_set_dp(arr, val, index, mem):
    key = "{}:{}".format(val, index)
    if key in mem:
        return mem[key]
    if val == 0:
        return 1
    elif val < 1:
        return 0
    elif index < 0:
        return 0
    elif arr[index] > val:
        to_return = sum_set_(arr, val, index-1, mem)
    else:
        to_return = sum_set_dp(arr, (val - arr[index]), index-1, mem) + sum_set_dp(arr, val, index-1, mem) 
    mem[key] = to_return
    
    return to_return

 
def sum_set(arr, val):
    # return sum_set_(arr, val, len(arr) -1)
    mem = {}
    return sum_set_dp(arr, val, len(arr) -1, mem)





print(sum_set([2,4,6,10], 16))
print(sum_set([1,2,3,3], 6))