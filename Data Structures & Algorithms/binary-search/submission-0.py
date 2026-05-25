class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            loc = (l+r) // 2
            num = nums[loc]
            if num == target:
                return loc
            elif num < target:
                l = loc+1
            else:
                r = loc - 1
        return -1