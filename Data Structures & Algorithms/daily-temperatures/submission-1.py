class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            curr_temp = temperatures[i]
            while stack and stack[-1][0] <= curr_temp:
                stack.pop()
            if not stack:
                ans[i] = 0
            else:
                ans[i] = stack[-1][1] - i
            stack.append((curr_temp, i))
        return ans