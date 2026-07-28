# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        stack = []
        ans = []
        while curr or stack:
            while curr:
                stack.append(curr)
                ans.append(curr.val)
                curr = curr.left
            curr = stack.pop().right
        return ans
