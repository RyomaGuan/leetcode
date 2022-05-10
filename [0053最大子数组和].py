class Solution:
    def maxSubArray(self, nums):
        total = maxTotal = nums[0]
        for num in nums[1:]:
            total = max(0, total) + num
            maxTotal = max(maxTotal, total)
        return maxTotal
