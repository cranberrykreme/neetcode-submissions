class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []
        count_stack = []
        k = 0
        ans = ''

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == '[':
                string_stack.append(ans)
                count_stack.append(k)
                ans = ''
                k = 0
            elif c == ']':
                temp = ans
                ans = string_stack.pop()
                count = count_stack.pop()
                ans += temp * count
            else:
                ans += c

        return ans