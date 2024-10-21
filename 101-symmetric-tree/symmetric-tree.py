class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            return (t1.val == t2.val) and \
                   is_mirror(t1.left, t2.right) and \
                   is_mirror(t1.right, t2.left)
        return is_mirror(root, root)
