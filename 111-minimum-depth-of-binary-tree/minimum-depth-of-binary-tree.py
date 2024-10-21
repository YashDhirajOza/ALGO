
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_r = self.minDepth(root.left)
        right_r = self.minDepth(root.right)
        if root.left is None:
            return right_r + 1
        elif root.right is None:
            return left_r + 1
        return min(left_r, right_r) + 1
