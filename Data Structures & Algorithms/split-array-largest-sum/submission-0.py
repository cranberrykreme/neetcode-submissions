class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = max(nums), sum(nums)
        max_count = 0
        while l <= r:
            m = l + (r-l)//2
            i, curr_sum, arr_count = 0, 0, 1
            while i < n:
                val = nums[i]
                if (curr_sum + val) > m:
                    curr_sum = val
                    i += 1
                    arr_count += 1
                else:
                    curr_sum += val
                    i += 1
            if arr_count <= k:
                max_count = m
                r = m - 1
            else:
                l = m + 1
        return max_count