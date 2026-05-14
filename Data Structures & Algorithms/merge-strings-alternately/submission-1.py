class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        n, m = len(word1), len(word2)
        for i in range(max(n, m)):
            if i < n:
                ans.append(word1[i])
            if i < m:
                ans.append(word2[i])
        return "".join(ans)