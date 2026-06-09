class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        ans = []
        for p in paths:
            if p == '..':
                if ans:
                    ans.pop()
            elif p == '' or p == '.':
                continue
            else:
                ans.append(p)
        return '/' + '/'.join(ans)