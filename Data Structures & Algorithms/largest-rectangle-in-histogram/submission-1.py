class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        ans = 0
        for i in range(n+1):
            start_loc = i
            while stack and (i == n or stack[-1][0] >= heights[i]):
                height, loc = stack.pop()
                width = i - loc
                ans = max(ans, height * width)
                start_loc = loc
            if i != n:
                stack.append((heights[i], start_loc))
        return ans