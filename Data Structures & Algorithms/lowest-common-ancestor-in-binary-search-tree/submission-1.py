# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root
        while node:
            curr = node.val
            if curr < p.val and curr < q.val:
                node = node.right
            elif curr > p.val and curr > q.val:
                node = node.left
            else:
                return node
        return None