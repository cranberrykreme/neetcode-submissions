class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        ans = []
        for i, num in enumerate(nums):
            if num > target:
                break
            if (i > 0 and num == nums[i-1]):
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l, r = j+1, n-1
                while l < r:
                    curr_sum = num + nums[j] + nums[l] + nums[r]
                    if curr_sum > target:
                        r -= 1
                    elif curr_sum < target:
                        l += 1
                    else:
                        ans.append([num, nums[j], nums[l], nums[r]])
                        r -= 1
                        l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
        return ans