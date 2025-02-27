import sys
def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    nums.sort()
    sum_ = None
    result = sys.maxsize
    if len(nums) == 3:
        return sum(nums)
    # if nums[0] >= 0:
    #     return sum([nums[0], nums[1], nums[2]])

    for idx in range(len(nums)):
        left = idx + 1
        #sub_arr = nums[left:]
        right = len(nums) - 1
        # print("Subarrays: ", nums[idx], "and ", sub_arr)
        while left < right :
            sum_ = nums[idx] + nums[left] + nums[right]
            if sum_ == target:
                result = sum_
                return result
            
            abs_dif = abs(target - sum_)
            if abs_dif < abs(target - result):
                result = sum_
            print("abs(target - sum_): ", abs(target - sum_), "and abs(target - result) ", abs(target - result)) 
            if sum_ < target:
                left += 1
            else:
                right -= 1
    return result

if __name__ == '__main__':
    nums = [-1,2,1,-4]
    target = 1
    print(threeSumClosest(nums, target))
    