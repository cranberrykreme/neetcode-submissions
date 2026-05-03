class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        end_idx = 0
        ans = []
        while end_idx < len(s):
            idx = int(s.index('#', end_idx))
            length = int(s[end_idx:idx])
            end_idx = idx+1 + length
            ans.append(s[idx+1:end_idx])
        return ans
