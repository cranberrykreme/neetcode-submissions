class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        curr_size = 1
        while curr_size < n:
            left_start = 0
            while left_start < n-1:
                mid = min(left_start + curr_size - 1, n - 1)
                right_end = min(left_start + 2 * curr_size - 1, n - 1)

                self._merge(nums, ans, left_start, mid, right_end)
                left_start += 2 * curr_size
            curr_size *= 2

        return nums


    def _merge(self, nums: List[int], arr: List[int], left: int, mid: int, right: int):
        for i in range(left, right+1):
            arr[i] = nums[i]
        
        l, r = left, mid+1
        for i in range(left, right + 1):
            if l > mid:
                nums[i] = arr[r]; r += 1
            elif r > right:
                nums[i] = arr[l]; l += 1
            elif arr[l] <= arr[r]:
                nums[i] = arr[l]; l += 1
            else:
                nums[i] = arr[r]; r += 1


