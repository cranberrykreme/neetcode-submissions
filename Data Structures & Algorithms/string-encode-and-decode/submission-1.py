class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i < len(s):
            idx = s.index('#', i)
            length = int(s[i:idx])
            i = idx+1 + length
            ans.append(s[idx+1:i])
        return ans
