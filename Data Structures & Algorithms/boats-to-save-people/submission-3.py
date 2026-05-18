class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        max_weight = max(people)
        w_count = [0] * (max_weight+1)
        for p in people:
            w_count[p] += 1
        loc = 0
        for i in range(len(w_count)):
            while w_count[i] > 0:
                people[loc] = i
                w_count[i] -= 1
                loc += 1
        ans = 0
        l, r = 0, len(people)-1
        while l <= r:
            curr_sum = people[l] + people[r]
            if curr_sum <= limit:
                l += 1
            r -= 1
            ans += 1
        return ans