from typing import List

# Coin change with repeatations of coins
# Numbers of ways to make a coin change, with infinite numbers of coins
def coin_change(arr :List, w: int):
    arr_len = len(arr)
    w_arr = [i for i in range(w+1)]
    # combination = [[0]*(w+1)]*arr_len # has an inbuilt python bug. This is because of shallow copy
    combination = [[0 for i in range(w + 1)] for j in range(arr_len)]
    # print(w_arr)
    # print(combination)
    for row_num  in range(arr_len) :
        for col_num in w_arr:
            if row_num == 0:
                if (col_num % arr[row_num] == 0):
                    combination[row_num][col_num] = 1
                else:
                    combination[row_num][col_num] = 0
            elif(arr[row_num] > col_num):
                combination[row_num][col_num] = combination[row_num - 1][col_num]
            else:
                prev_value = combination[row_num - 1][col_num]
                ref_col = col_num - arr[row_num]
                ref_val = combination[row_num ][ref_col]
                combination[row_num][col_num] = prev_value + ref_val
    print(combination)
    print("Answer: ", combination[arr_len-1][w])
    
coin = [2,3,5,10]
w = 15

coin_change(coin, w)    