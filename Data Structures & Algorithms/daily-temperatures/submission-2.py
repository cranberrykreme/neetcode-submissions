class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                to_add_loc = stack[-1][1]
                ans[to_add_loc] = i - to_add_loc
                stack.pop()
            stack.append((temp, i))
        return ans