class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        right_elem = len(nums)-1
        k = 0
        while k <= right_elem:
            num = nums[k]
            while right_elem >= 0 and nums[right_elem] == val:
                right_elem -= 1
            if num == val:
                nums[k], nums[right_elem] = nums[right_elem], nums[k]
                right_elem -= 1
            else:
                k += 1
        return k