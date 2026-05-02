class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums))]
        freq: dict[int, int] = defaultdict(int)

        for num in nums:
            new_freq = freq[num]
            freq[num] += 1
            buckets[new_freq].append(num)
            if new_freq > 0:
                buckets[new_freq-1].remove(num)

        num_vars = 0
        ans = []
        idx = len(nums)-1
        while num_vars < k:
            curr_freq = buckets[idx]
            for var in curr_freq:
                ans.append(var)
                num_vars += 1
            idx -= 1

        return ans
