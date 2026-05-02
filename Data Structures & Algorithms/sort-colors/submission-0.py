class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, ones, twos = 0, 0, 0
        for num in nums:
            if num==0:
                zeros += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1
        
        for i in range(zeros):
            nums[i] = 0
        for i in range(zeros, ones+zeros):
            nums[i] = 1
        for i in range(zeros+ones, len(nums)):
            nums[i] = 2
        