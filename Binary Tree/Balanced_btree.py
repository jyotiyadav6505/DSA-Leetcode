class Solution(object):
    def isBalanced(self, root):

        def height(node):

            if node == None:
                return 0

            LH = height(node.left)
            RH = height(node.right)

            if LH == -1 or RH == -1:
                return -1

            if abs(LH - RH) > 1:
                return -1

            return 1 + max(LH, RH)

        return height(root) != -1