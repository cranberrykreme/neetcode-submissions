class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # find partition
        n = mountainArr.length()
        l, r = 0, n - 1
        partition = -1
        while l <= r:
            m = l + (r-l)//2
            lm = float("-inf") if m <= 0 else mountainArr.get(m-1)
            rm = float("inf") if m >= n-1 else mountainArr.get(m+1)
            mid = mountainArr.get(m)
            if mid > lm and mid > rm:
                partition = m
                break
            elif lm > mid:
                r = m - 1
            else:
                l = m + 1
        
        l, r = 0, partition
        while l <= r:
            m = l + (r-l)//2
            m_val = mountainArr.get(m)
            if m_val == target:
                return m
            elif m_val > target:
                r = m - 1
            else:
                l = m + 1
        
        l, r = partition+1, n-1
        while l <= r:
            m = l + (r-l)//2
            m_val = mountainArr.get(m)
            if m_val == target:
                return m
            elif m_val > target:
                l = m + 1
            else:
                r = m - 1
        return -1
