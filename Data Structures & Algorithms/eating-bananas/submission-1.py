class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_eat = 1
        max_eat = max(piles)
        speed = 0

        while min_eat <= max_eat:
            try_speed = (min_eat + max_eat) // 2
            time_to_eat = 0
            for pile in piles:
                time_to_eat += math.ceil(pile / try_speed)
            if time_to_eat <= h:
                max_eat = try_speed - 1
                speed = try_speed
            else:
                min_eat = try_speed + 1

        return speed