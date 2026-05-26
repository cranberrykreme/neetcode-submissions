class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortest_window = ""
        left_wall = 0
        target_count = {}
        curr_count = {}
        curr_hits = 0

        for c in t:
            target_count[c] = target_count.get(c, 0) + 1

        for i in range(len(s)):
            curr = s[i]
            target_count_of_curr = target_count.get(curr, 0)
            curr_count_of_curr = curr_count.get(curr, 0)
            if target_count_of_curr > 0:
                curr_count_of_curr += 1
                if curr_count_of_curr <= target_count_of_curr:
                    curr_hits += 1
                curr_count[curr] = curr_count_of_curr
            while curr_hits == len(t):
                if len(shortest_window) == 0 or len(shortest_window) > i-left_wall:
                    shortest_window = s[left_wall:i+1]
                left_char_target_count = target_count.get(s[left_wall], 0)
                left_char_curr_count = curr_count.get(s[left_wall], 0)
                if 0 < left_char_target_count:
                    if left_char_target_count >= left_char_curr_count:
                        curr_hits -= 1
                    curr_count[s[left_wall]] = left_char_curr_count - 1
                left_wall += 1

        return shortest_window