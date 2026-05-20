class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        sequence = 0
        longest_sequence = 0
        for i, c in enumerate(s):
            if c not in chars:
                chars.add(c)
                sequence += 1
                longest_sequence = max(sequence, longest_sequence)
            else:
                left_wall = i - sequence
                while s[left_wall] != c:
                    sequence -= 1
                    chars.remove(s[left_wall])
                    left_wall += 1
        return longest_sequence