from typing import List


def min_coin_change_ways(arr: List, w: int):
    
    arr_len = len(arr)
    col_val = w + 1
    table = [ [0 for i in range(col_val)] for j in range(arr_len)]
    # print(table)
    for i in range(arr_len):
        for j in range(col_val):
            if i == 0:
                table[i][j] = j
            elif arr[i] > j :
                table[i][j] = table[i-1][j]
            else:
                # 1 -> means that you already selected the coin in i,j position
                table[i][j] = min(table[i-1][j], 1 + table[i][j - arr[i]])
    print(table)
    
    
coins = [1,5,6,9]
change = 10
min_coin_change_ways(coins, change)