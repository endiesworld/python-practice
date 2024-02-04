"""
    For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given a roman numeral, convert it to an integer.
    
"""
import sys

class Solution:
    def romanToInt(self, s: str) -> int:
        rom_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        prev = sys.maxsize
        process = '0'
        for data in s:
            if (int(prev) >= int(rom_int.get(data, 0))):
                process += f"+ ({rom_int[data]})"
                result += int(rom_int[data])
                prev = rom_int[data]
                
            else:
                process += f"+ ({rom_int[data]}) + (-2 * {prev})"
                result += (int(rom_int[data]) - (2 * int(prev)))
                prev = rom_int[data]
               
        # result = eval(process)
        return result

if __name__ == '__main__':
    test_case = Solution()
    
    assert test_case.romanToInt("MCMXCIV") == 1994