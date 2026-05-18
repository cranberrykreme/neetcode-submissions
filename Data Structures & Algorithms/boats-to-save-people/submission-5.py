class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        w_count = [0] * (limit+1)
        for p in people:
            w_count[p] += 1
        ans = 0
        l, r = 0, limit
        while l <= r:
            while l <= r and w_count[l] == 0:
                l += 1
            while l <= r and w_count[r] == 0:
                r -= 1
            if l > r:
                break
            ans += 1
            w_count[r] -= 1

            if (l + r) <= limit and w_count[l] > 0:
                w_count[l] -= 1
            
        return ans