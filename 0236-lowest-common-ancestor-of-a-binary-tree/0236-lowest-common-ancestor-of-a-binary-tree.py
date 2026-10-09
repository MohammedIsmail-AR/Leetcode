# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':

        # If there is no node, or we found p/q,
        # return the current node.
        if root is None or root == p or root == q:
            return root

        # Search the left subtree
        left = self.lowestCommonAncestor(root.left, p, q)

        # Search the right subtree
        right = self.lowestCommonAncestor(root.right, p, q)

        # One node was found on each side,
        # so the current root is the LCA.
        if left and right:
            return root

        # If only the left side found a node,
        # pass it upward.
        if left:
            return left

        # Otherwise, pass the right result upward.
        return right