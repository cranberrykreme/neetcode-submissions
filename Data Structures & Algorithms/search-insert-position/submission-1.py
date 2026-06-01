class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            loc = (l + r) // 2
            if nums[loc] == target:
                return loc
            elif nums[loc] < target:
                l = loc + 1
            else:
                r = loc - 1
        return l