class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        left_wall = 0
        longest_sequence = 0

        for i, c in enumerate(s):
            if c in chars and chars[c] >= left_wall:
                left_wall = chars[c] + 1
            else:
                longest_sequence = max(longest_sequence, i - left_wall + 1)
            chars[c] = i
        return longest_sequence