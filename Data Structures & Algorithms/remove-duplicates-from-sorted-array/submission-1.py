class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        if len(nums) == 1:
            return 1
        for i, num in enumerate(nums):
            if num != nums[i-1]:
                nums[k] = num
                k += 1
        return k