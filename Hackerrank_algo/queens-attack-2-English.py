#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    
        
    moves = 0
    
    def vertical_up(moves):
        up = r_q
        while (up < n ):
            up += 1
            if ([up, c_q] in obstacles):
                break
            moves += 1
        return moves
        
    def vertical_down(moves):
        down = r_q
        while (down > 1):
            down -= 1
            if ([down, c_q] in obstacles):
                break
            moves += 1
        return moves
        
    def horizontal_right(moves):
        right = c_q
        while (right < n ):
            right += 1
            if ([ r_q, right] in obstacles):
                break
            moves += 1
        return moves
        
    def horizontal_left(moves):
        left = c_q
        while (left > 1 ):
            left -= 1
            if ([r_q, left] in obstacles):
                break
            moves += 1
        return moves
        
    def dig_right_up(moves):
        up = r_q
        right = c_q
        while ((up < n and right < n) ):
            up += 1
            right += 1
            if ([up, right] in obstacles):
                break
            moves += 1
        return moves
        
    def dig_right_down(moves):
        down = r_q
        right = c_q
        while ((down > 1 and right < n) ):
            down -= 1
            right += 1
            if ([down, right] in obstacles):
                break
            moves += 1
        return moves
            
    def dig_left_up(moves):
        up = r_q
        left = c_q
        while ((up < n and left > 1) ):
            up += 1
            left -= 1
            if ([up, left] in obstacles):
                break
            moves += 1
        return moves
        
    def dig_left_down(moves):
        down = r_q
        left = c_q
        while ((down > 1 and left > 1) ):
            down -= 1
            left -= 1
            if ([down, left] in obstacles):
                break
            moves += 1
        return moves
            
    moves = vertical_up(moves)
    moves = vertical_down(moves)
    moves = horizontal_right(moves)
    moves = horizontal_left(moves)
    moves = dig_right_up(moves)
    moves = dig_right_down(moves)
    moves = dig_left_up(moves)
    moves = dig_left_down(moves)
    
    return moves
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
