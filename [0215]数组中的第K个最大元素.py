def partition(left, right, nums):
    i, baseNum = left, nums[right]
    # < baseNum 右边界, > baseNum 左边界
    l, r = left - 1, right + 1
    while i < r:
        if nums[i] == baseNum:
            i += 1
        elif nums[i] < baseNum:
            l += 1
            nums[l], nums[i] = nums[i], nums[l]
            i += 1
        else:
            r -= 1
            nums[i], nums[r] = nums[r], nums[i]
    return l + 1, r - 1


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        # 返回值的索引
        k = len(nums) - k
        # 快排的左右边界
        left, right = 0, len(nums) - 1
        # 已排序的左右边界
        l, r = partition(left, right, nums)
        while not l <= k <= r:
            if k < l:
                right = l - 1
            else:
                left = r + 1
            l, r = partition(left, right, nums)
        return nums[k]
