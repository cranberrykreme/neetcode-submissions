class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        entries = set()
        for i, num in enumerate(nums):
            l, r = i+1, len(nums)-1
            while l < r:
                curr_sum = num + nums[l] + nums[r]
                if curr_sum == 0 and (num, nums[l], nums[r]) not in entries:
                    ans.append([num, nums[l], nums[r]])
                    entries.add((num, nums[l], nums[r]))
                    l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    l += 1
        return ans