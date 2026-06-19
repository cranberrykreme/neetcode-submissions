class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}
        for i, num in enumerate(nums):
            other = found.get(target-num, -1)
            if other > -1:
                return [other, i]
            found[num] = i
        return [0]