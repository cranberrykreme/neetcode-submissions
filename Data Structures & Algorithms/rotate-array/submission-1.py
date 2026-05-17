class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        ans = [0] * len(nums)
        for i, num in enumerate(nums):
            ans[(i+k)%len(nums)] = num
        nums[:] = ans