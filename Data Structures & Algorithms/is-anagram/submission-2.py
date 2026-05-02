class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)

        if len(s) != len(t):
            return False

        for st in s:
            d[st] += 1
        
        for ts in t:
            if d[ts] < 1:
                return False
            d[ts] -= 1

        for k,v in d.items():
            if v != 0:
                return False

        return True