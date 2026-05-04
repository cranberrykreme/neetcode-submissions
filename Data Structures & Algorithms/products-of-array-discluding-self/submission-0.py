class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = 1
        left_prod_arr = [0] * len(nums)
        for i, num in enumerate(nums):
            left_prod *= num
            left_prod_arr[i] = left_prod
        
        ans = [0] * len(nums)
        right_prod = nums[-1]
        ans[-1] = left_prod_arr[-2]
        for i in range(len(nums)-2, 0, -1):
            ans[i] = right_prod * left_prod_arr[i-1]
            right_prod *= nums[i]
        ans[0] = right_prod
        return ans