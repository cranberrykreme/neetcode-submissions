class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        ans = 0
        for i, h in enumerate(heights + [0]):
            start_loc = i
            while stack and (i == n or stack[-1][0] >= h):
                height, loc = stack.pop()
                width = i - loc
                ans = max(ans, height * width)
                start_loc = loc
            stack.append((h, start_loc))
        return ans