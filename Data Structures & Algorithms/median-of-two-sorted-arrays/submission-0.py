class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1)-1
        while True:
            take_from_one = l + (r-l)//2
            take_from_two = half - take_from_one - 2

            a_left = nums1[take_from_one] if take_from_one >= 0 else float("-inf")
            a_right = nums1[take_from_one+1] if (take_from_one+1) < len(nums1) else float("inf")
            b_left = nums2[take_from_two] if take_from_two >= 0 else float("-inf")
            b_right = nums2[take_from_two+1] if (take_from_two+1) < len(nums2) else float("inf")

            if a_left <= b_right and b_left <= a_right:
                if total % 2:
                    return min(a_right, b_right)
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                r = take_from_one - 1
            else:
                l = take_from_one + 1