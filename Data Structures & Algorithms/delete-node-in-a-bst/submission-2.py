# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        prev = None
        curr = root
        while curr:
            if curr.val > key:
                prev = curr
                curr = curr.left
            elif curr.val < key:
                prev = curr
                curr = curr.right
            else: # remove node
                if not curr.left or not curr.right:
                    child = curr.left if curr.left else curr.right
                    if not prev:
                        return child
                    if prev.left == curr:
                        prev.left = child
                    else:
                        prev.right = child
                    return root
                par = None
                to_remove = curr
                curr = curr.right
                while curr.left:
                    par = curr
                    curr = curr.left
                
                if par:
                    par.left = curr.right
                    curr.right = to_remove.right

                curr.left = to_remove.left

                if not prev:
                    return curr
                
                if prev.left == to_remove:
                    prev.left = curr
                else:
                    prev.right = curr
                return root
        return root