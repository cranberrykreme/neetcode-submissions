class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            curr_temp = temperatures[i]
            curr_compare = stack[-1] if stack else None
            while stack and curr_compare[0] <= curr_temp:
                stack.pop()
                curr_compare = stack[-1] if stack else None
            if not curr_compare:
                ans[i] = 0
            else:
                ans[i] = curr_compare[1] - i
            stack.append((curr_temp, i))
        return ans