class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []
        counter_stack = []
        curr_count = 0
        curr = ''
        
        for c in s:
            if c.isdigit():
                curr_count = curr_count*10 + int(c)
            elif c == '[':
                string_stack.append(curr)
                counter_stack.append(curr_count)
                curr = ''
                curr_count = 0
            elif c == ']':
                temp = curr
                curr = string_stack.pop()
                count = counter_stack.pop()
                curr += temp * count
            else:
                curr += c
        return curr