from collections import deque

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right, loc = 0, len(arr)-1, 0
        ans = deque([])
        while left <= right:
            loc = (left + right) // 2
            val = arr[loc]
            if val == x:
                break
            elif val < x:
                left = loc + 1
            else:
                right = loc - 1
        if arr[loc] > x:
            right = loc
            left = loc-1
        else:
            left = loc
            right = loc + 1
        
        while right - left <= k and right < len(arr) and left > -1:
            print(f"left => {left}, right => {right}")
            lower = abs(arr[left]-x)
            higher = abs(arr[right]-x)
            if higher < lower:
                ans.append(arr[right])
                right += 1
            else:
                ans.appendleft(arr[left])
                left -= 1
        while left > -1 and len(ans) < k:
            ans.appendleft(arr[left])
            left -= 1
        while right < len(arr) and len(ans) < k:
            ans.append(arr[right])
            right += 1
        return list(ans)

            



