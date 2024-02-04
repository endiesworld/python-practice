"""
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    

    Example 1:

    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    Example 2:

    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if len(strs) == 1:
        #     return strs[0]
        str_1 = strs[0]
        pref = ''
        str_1_len = len(str_1)
        end = False
        for data in range(str_1_len):
            for strn in strs:
                if data >= len(strn):
                    end = True 
                    break
                if str_1[data] != strn[data]:
                    end = True 
                    break
            if end:
                break
            pref += str_1[data]

        return pref


if __name__ == '__main__':
    test_case = Solution()
    
    assert test_case.longestCommonPrefix(["flower","flow","flight"]) == 'fl'
    assert test_case.longestCommonPrefix(["dog","racecar","car"]) == ''