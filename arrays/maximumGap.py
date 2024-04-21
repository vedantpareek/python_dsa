#https://leetcode.com/problems/maximum-gap/

class Solution(object):
    def maximumGap(self, nums):
        nums = sorted(nums)
        if len(nums) < 2:
            return 0
        max_diff = -1
        for i in range(len(nums)):
            if i <= len(nums) - 2:
                current_ele = nums[i]
                next_ele = nums[i + 1]
                current_gap = next_ele - current_ele
                if current_gap > max_diff:
                    max_diff = current_gap
        return max_diff


test_cases = [[3,6,9,1] , [10] , [1,2,3,4,5,6,100,7,99]]

for test_case in test_cases:
    print(Solution().maximumGap(test_case))
