class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        prefix = 1
        for i, num in enumerate(nums):
            ans[i] *= prefix
            prefix *= num
        
        suffix = 1
        print(ans)
        for i in range(n-1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans