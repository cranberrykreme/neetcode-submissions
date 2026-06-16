class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), math.ceil(len(weights)/days)*max(weights)
        min_weight = float('inf')
        while l <= r:
            days_loading = 1
            mid = l + (r-l)//2
            loc = 0
            space_left = mid
            while loc < len(weights):
                w = weights[loc]
                space_left -= w
                if space_left < 0:
                    days_loading += 1
                    space_left = mid - w
                loc += 1
            if days_loading <= days:
                min_weight = mid
                r = mid -1
            else:
                l = mid + 1
        return min_weight