class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left_wall = 0
        longest_sequence = 0
        chars_in_window = {}
        max_frequency = 0

        for i, c in enumerate(s):
            chars_in_window[c] = chars_in_window.get(c, 0) + 1
            max_frequency = max(max_frequency, chars_in_window[c])

            if (i - left_wall + 1) - max_frequency > k:
                chars_in_window[s[left_wall]] -= 1
                left_wall += 1

            longest_sequence = max(longest_sequence, i - left_wall + 1)
            i += 1
        return longest_sequence