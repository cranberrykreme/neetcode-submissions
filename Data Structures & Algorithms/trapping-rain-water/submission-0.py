class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        for i, h in enumerate(height):
            left_max[i] = max(left_max[i-1], height[i])
        right_max = 0
        water = 0
        for i in range(n-1, -1, -1):
            sides = min(left_max[i], right_max)
            max_hold = max(0, sides - height[i])
            water += max_hold
            right_max = max(right_max, height[i])
        return water