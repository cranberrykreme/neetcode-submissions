class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i, num in enumerate(nums):
            l, r = i+1, len(nums)-1
            if num > 0:
                break
            if i > 0 and num == nums[i-1]:
                continue
            while l < r:
                curr_sum = num + nums[l] + nums[r]
                if curr_sum == 0:
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    while l < r and nums[r+1] == nums[r]:
                        r -= 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    l += 1
        return ans