class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            mid = l + (r-l)//2

            days_loading = 1
            curr_load = 0
            
            for w in weights:
                curr_load += w
                if curr_load > mid:
                    days_loading += 1
                    curr_load = w

            if days_loading <= days:
                min_weight = mid
                r = mid -1
            else:
                l = mid + 1
        return min_weight