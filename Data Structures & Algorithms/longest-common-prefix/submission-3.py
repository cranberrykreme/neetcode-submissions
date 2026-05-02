class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sub_str = strs[0]

        for i in range(1, len(strs)):
            val = strs[i]
            if len(val) < 1: 
                sub_str = ''
            sub_str = sub_str[:len(val)]
            for k in range(min(len(sub_str), len(val))):
                if val[k] != sub_str[k]:
                    sub_str = sub_str[:k]
                    break
        return sub_str

        