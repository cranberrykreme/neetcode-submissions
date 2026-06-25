class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        total_size = len(nums1) + len(nums2)
        half = total_size // 2
        l, r = 0, len(nums1)-1
        while True:
            i = l + (r-l)//2
            j = half-i-2

            one_left = nums1[i] if i >= 0 else float("-inf")
            one_right = nums1[i+1] if (i+1) < len(nums1) else float("inf")
            two_left = nums2[j] if j >= 0 else float("-inf")
            two_right = nums2[j+1] if (j+1) < len(nums2) else float("inf")

            if one_left <= two_right and two_left <= one_right:
                if total_size % 2:
                    return min(one_right, two_right)
                return (min(one_right, two_right) + max(one_left, two_left)) / 2
            elif one_left > two_right:
                r = i - 1
            else:
                l = i + 1
