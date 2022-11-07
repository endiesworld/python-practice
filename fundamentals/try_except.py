
def calculate_mean(arr):
    count = 0
    sum_arr = 0

    for i in arr:
        try:
            sum_arr += i
            count += 1
        except TypeError:
            print(f'{i} is not an integer')
    return sum_arr / count


print(calculate_mean([5, 10, 'test', 5, 10]))
