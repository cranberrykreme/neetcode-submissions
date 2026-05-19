class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i, num in enumerate(nums):
            j = i+1
            while j < len(nums) and j-i <= k:
                if nums[j] == num:
                    return True
                j += 1
        return False