class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            l_char = s[left]
            r_char = s[right]
            while not l_char.isalnum() and left < len(s)-1:
                left += 1
                l_char = s[left]
            while not r_char.isalnum() and right >= 0:
                right -= 1
                r_char = s[right]
            if left < right:
                if l_char.casefold() != r_char.casefold():
                    return False
            left += 1
            right -= 1
        return True