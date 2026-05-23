class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        shortest_len = len(nums) + 1
        curr_sum = 0
        l = 0

        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                shortest_len = min(shortest_len, r-l+1)
                curr_sum -= nums[l]
                l += 1
        
        return 0 if shortest_len > len(nums) else shortest_len