class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if val not in nums:
            return len(nums)
        right = len(nums) - 1
        left = 0
        while left <= right:
            num = nums[left]
            if num == val:
                while left < right and nums[right] == val:
                    right -=1
                hold = nums[right]
                nums[right] = num
                nums[left] = hold
            left += 1
        print(f'left -> {left}, right -> {right}')
        return right