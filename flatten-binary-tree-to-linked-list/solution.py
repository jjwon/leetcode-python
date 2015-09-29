# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # flatten left and right, and then concatenate left and right on the right side
        head = root
        if root:
            self.flatten(root.left)
            self.flatten(root.right)
            tmp = root.right
            root.right = root.left
            root.left = None
            while root.right:
                root = root.right
            root.right = tmp
        return head

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    result = Solution().flatten(root)
    print result.val
    print result.right.val
    print result.right.right.val
    print result.right.right.right.val
    print result.right.right.right.right.val
    print result.right.right.right.right.right.val
