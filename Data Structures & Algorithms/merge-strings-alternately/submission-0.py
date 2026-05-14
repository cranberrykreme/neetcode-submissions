class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        ans = ""
        while i < len(word1) and i < len(word2):
            ans += word1[i] + word2[i]
            i += 1
        if i < len(word1):
            ans += word1[i:]
        if i < len(word2):
            ans += word2[i:]
        return ans