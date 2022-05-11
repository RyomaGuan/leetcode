class Solution:
    def twoSum(self, nums, target: int):
        num2idx = dict()
        for i in range(len(nums)):
            if target - nums[i] in num2idx:
                return [num2idx[target - nums[i]], i]
            else:
                num2idx[nums[i]] = i
