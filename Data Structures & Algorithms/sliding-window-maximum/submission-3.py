class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        left_wall = right_wall = 0
        max_queue = deque()
        while right_wall < len(nums):
            while max_queue and nums[right_wall] > nums[max_queue[-1]]:
                max_queue.pop()
            max_queue.append(right_wall)
            if (right_wall - left_wall + 1) >= k:
                if max_queue[0] < left_wall:
                    max_queue.popleft()
                ans.append(nums[max_queue[0]])
                left_wall += 1
            right_wall += 1
        return ans