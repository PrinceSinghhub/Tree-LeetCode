# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root):
        ans = []

        if root == None:
            return ans

        ans += self.dfs(root.left)
        ans.append(root.val)
        ans += self.dfs(root.right)

        return set(ans)

    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return len(self.dfs(root)) == 1


# another approch without using extran space

class Solution1:

    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        if root.left:

            if root.val != root.left.val:
                return False

        if root.right:

            if root.val != root.right.val:
                return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
