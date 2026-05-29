class Solution:
    def isValid(self, s: str) -> bool:
        keys = {')':'(', ']':'[', '}':'{'}
        stack = []
        for c in s:
            if c in {'(', '[', '{'}:
                stack.append(c)
            elif len(stack) > 0:
                openner = stack.pop()
                if keys[c] != openner:
                    return False
            else:
                return False
        return True if len(stack) == 0 else False