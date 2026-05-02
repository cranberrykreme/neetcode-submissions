class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = candidate = 0
        for i, num in enumerate(nums):
            if i == 0:
                res = num
            if num != res:
                candidate -= 1
            else:
                candidate += 1
            if candidate < 1:
                res = num
                candidate = 1
        return res