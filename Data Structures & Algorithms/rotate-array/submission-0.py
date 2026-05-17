class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans = [0] * len(nums)
        for i, num in enumerate(nums):
            ans[(i+k)%len(nums)] = num
        for i in range(len(ans)):
            nums[i] = ans[i]