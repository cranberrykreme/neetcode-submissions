class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_sequence = 0
        left = 0
        counts = {}
        max_frequency = 0
        
        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            
            max_frequency = max(max_frequency, counts[s[right]])
            
            if (right - left + 1) - max_frequency > k:
                counts[s[left]] -= 1
                left += 1
            
            longest_sequence = max(longest_sequence, right - left + 1)
            
        return longest_sequence