"""

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""


def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        sum_store = []
        last_1 =None
        last_2 = None
        last_3 = None
        combination_store = {}
        
        for idx in range(len(nums)): 
            sub_start = idx + 1
            sub_arr = nums[sub_start:]

            left = 0
            right = len(sub_arr) -1

            while(left < right):
                sum_ = sub_arr[left] +  sub_arr[right] + nums[idx]
                if(sum_ ==  0):
                    if( str(nums[idx]) + str(sub_arr[left]) + str(sub_arr[right]) in combination_store ):
                        left += 1
                        continue
                    sum_store.append([nums[idx], sub_arr[left],  sub_arr[right]])
                    last_1 = nums[idx]
                    last_2 = sub_arr[left]
                    last_3 = sub_arr[right]
                    combination = str(last_1) + str(last_2) + str(last_3)
                    combination_store[combination] = 1
                    left += 1
                elif( sum_ > 0 ):
                    right -= 1
                else:
                    left += 1


        return  sum_store