class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        l = len(pref)

        for s in strs:
            while s[0:l] != pref[0:l]:
                l -= 1
        return pref[0:l]

        