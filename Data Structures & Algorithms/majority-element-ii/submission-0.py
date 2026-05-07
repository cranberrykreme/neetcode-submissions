class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cutoff = len(nums) // 3
        ans = []
        d = {}

        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        for key, count in d.items():
            if count > cutoff:
                ans.append(key)
        return ans