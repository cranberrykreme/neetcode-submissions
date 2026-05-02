class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        left_pointer = right_pointer = 0
        cutoff = len(nums) // 2
        left_list, right_list = self.sortArray(nums[:cutoff]), self.sortArray(nums[cutoff:])

        while left_pointer < len(left_list) and right_pointer < len(right_list):
            if left_list[left_pointer] <= right_list[right_pointer]:
                nums[left_pointer + right_pointer] = left_list[left_pointer]
                left_pointer += 1
            else:
                nums[left_pointer + right_pointer] = right_list[right_pointer]
                right_pointer += 1
        
        while left_pointer < len(left_list):
            nums[left_pointer + right_pointer] = left_list[left_pointer]
            left_pointer += 1
        
        while right_pointer < len(right_list):
            nums[left_pointer + right_pointer] = right_list[right_pointer]
            right_pointer += 1

        return nums

