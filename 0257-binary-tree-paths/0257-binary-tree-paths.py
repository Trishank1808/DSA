class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode], path="", result=None) -> List[str]:
        if result is None:
            result = []       
        if root:
            path += str(root.val)
            if not root.left and not root.right:
                result.append(path)
            else:
                self.binaryTreePaths(root.left, path + "->", result)
                self.binaryTreePaths(root.right, path + "->", result)
        return result