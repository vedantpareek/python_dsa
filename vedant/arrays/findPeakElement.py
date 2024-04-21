#https://leetcode.com/problems/find-peak-element/
class Solution(object):
    def findPeakElement(self, nums):
        if len(nums) ==2:
            return 0 if nums[0]>nums[1] else 1
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            if i >= 1 and i <= len(nums) - 2:
                if nums[i - 1] < nums[i] > nums[i + 1]:
                    return i
            if i == len(nums) - 1:
                if nums[i] > nums[i-1]:
                    return i
            i += 1
        return 0


test_cases = [[1,2],[1,2,3,1],[1,2,1,3,5,6,4]]
for test_case in test_cases:
    print(Solution().findPeakElement(test_case))
