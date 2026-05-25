class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        longest_substring = 0
        max_curr_count = 0
        left_wall = 0

        for i, c in enumerate(s):
            char_count[c] = char_count.get(c, 0) + 1
            max_curr_count = max(max_curr_count, char_count[c])

            while (i-left_wall+1) > max_curr_count+k:
                char_count[s[left_wall]] -= 1
                left_wall += 1
            longest_substring = max(longest_substring, (i-left_wall+1))
        return longest_substring