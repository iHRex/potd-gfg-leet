# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def largestValuesHelper(root, depth, result):
            if not root:
                return
            if depth == len(result):
                result.append(root.val)
            else:
                result[depth] = max(result[depth], root.val)
            largestValuesHelper(root.left, depth+1, result)
            largestValuesHelper(root.right, depth+1, result)

        result = []
        largestValuesHelper(root, 0, result)
        return result
        