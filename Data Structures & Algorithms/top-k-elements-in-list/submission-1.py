class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        freq: dict[int, int] = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        for num, count in freq.items():
            buckets[count].append(num)

        ans = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                ans.append(num)
            if len(ans) == k:
                return ans

        return []
