class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        shortest_len = len(nums) + 1
        curr_sum = 0
        l = r = 0
        while r < len(nums) and l <= r:
            curr_sum += nums[r]
            if (curr_sum) >= target:
                curr_sum -= (nums[r] + nums[l])
                shortest_len = min(shortest_len, r-l+1)
                l += 1
                continue
            r += 1
        
        if shortest_len > len(nums):
            return 0
        return shortest_len