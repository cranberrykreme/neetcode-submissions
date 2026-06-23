class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        while l <= r:
            m = l + (r-l)//2

            arr_count = 1
            curr_count = 0
            for num in nums:
                if curr_count + num > m:
                    curr_count = num
                    arr_count += 1
                else:
                    curr_count += num
            
            if arr_count <= k:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res