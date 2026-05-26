class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left_wall = 0
        target_count = {}
        curr_count = {}
        hits = 0

        for c in t:
            target_count[c] = target_count.get(c, 0) + 1

        res, res_len = [0,0], float('inf')
        for i in range(len(s)):
            curr = s[i]
            curr_count[curr] = curr_count.get(curr, 0) + 1
            if curr in target_count and curr_count[curr] <= target_count[curr]:
                hits += 1

            while hits == len(t):
                if res_len > i-left_wall+1:
                    res, res_len = [left_wall, i+1], i-left_wall+1
                curr_count[s[left_wall]] -= 1
                if s[left_wall] in target_count and target_count[s[left_wall]] > curr_count[s[left_wall]]:
                    hits -= 1
                left_wall += 1

        return "" if res_len == float('inf') else s[res[0]:res[1]]