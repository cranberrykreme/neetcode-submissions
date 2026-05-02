class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[right] == val:
                right -= 1
                continue
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                continue
            left += 1
        return left