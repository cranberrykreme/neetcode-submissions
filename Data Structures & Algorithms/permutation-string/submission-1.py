class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_len = len(s1)
        s2_len = len(s2)
        if target_len > s2_len:
            return False

        target_char_count = [0] * 26

        for i in range(target_len):
            target_char_count[(ord(s1[i])%32)-1] += 1
        
        left_wall = 0
        found_chars = [0] * 26
        for i in range(s2_len):
            found_chars[(ord(s2[i])%32)-1] += 1
            if (i - left_wall + 1) > target_len:
                found_chars[(ord(s2[left_wall])%32)-1] -= 1
                left_wall += 1
            if target_char_count == found_chars:
                return True

        return False