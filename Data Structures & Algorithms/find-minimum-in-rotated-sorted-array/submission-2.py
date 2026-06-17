class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            r_val, mid_val = nums[r], nums[mid]
            if r_val < mid_val:
                l = mid+1
            else:
                r = mid
        return nums[r]