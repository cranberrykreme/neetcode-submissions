class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            num = nums[i]
            if num > 0 and num < n and nums[num-1] != num:
                nums[i], nums[num-1] = nums[num-1], nums[i]
                i -= 1
            i += 1
        ans = n+1
        for i, num in enumerate(nums):
            if num != i+1:
                return i+1
        return ans
                