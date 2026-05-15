class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            num = nums[i]
            if num != nums[i-1]:
                nums[k] = num
                k += 1
        return k