class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        for i, h in enumerate(heights):
            start_loc = i
            while stack and stack[-1][0] >= h:
                height, loc = stack.pop()
                width = i - loc
                ans = max(ans, height * width)
                start_loc = loc
            stack.append((h, start_loc))
        max_len = len(heights)
        for h, start_loc in stack:
            width = max_len - start_loc
            ans = max(ans, width * h)
        return ans