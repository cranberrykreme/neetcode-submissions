class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicates = set()
        for i, num in enumerate(nums):
            if i > k:
                duplicates.remove(nums[i-k-1])
            
            if num in duplicates:
                return True
            duplicates.add(num)

        return False