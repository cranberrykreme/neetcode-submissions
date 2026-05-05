class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)
        consecutive = 0
        for val in vals:
            if val-1 not in vals:
                curr = 0
                while val in vals:
                    curr += 1
                    val += 1
                if curr > consecutive:
                    consecutive = curr
        return consecutive