class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        max_elem = 0
        for num in nums:
            d[num] += 1
            if d[num] > d[max_elem]:
                max_elem = num
        return max_elem