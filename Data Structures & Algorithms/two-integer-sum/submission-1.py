class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, num in enumerate(nums):
            needed = target - num
            if needed in d:
                return [d[needed], i]
            d[num] = i
        return []
            