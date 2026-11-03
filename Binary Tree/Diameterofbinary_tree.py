class Solution(object):
    def diameterOfBinaryTree(self, root):

        self.diameter = 0

        def solve(node):
            if node == None:
                return 0

            LH = solve(node.left)
            RH = solve(node.right)

            self.diameter = max(self.diameter, LH + RH)

            return 1 + max(LH, RH)

        solve(root)

        return self.diameter