class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        i = 0
        ans = []
        while i < len(nums) - 2 and nums[i] <= 0:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[j] + nums[k] > -nums[i]:
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < len(nums) and nums[j - 1] == nums[j]:
                        j += 1
                    while k > i and nums[k + 1] == nums[k]:
                        k -= 1
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
        return ans
