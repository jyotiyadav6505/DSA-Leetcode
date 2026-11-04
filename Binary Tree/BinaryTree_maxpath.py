class Solution(object):
    def maxPathSum(self, root):
        maxi = [float('-inf')]

        def solve(node):
            

            if node is None:
                 return 0

            leftSum = solve(node.left)
            if leftSum < 0:
                leftSum = 0

            rightSum = solve(node.right)
            if rightSum < 0:
                rightSum = 0

            maxi[0] = max(maxi[0], leftSum + node.val + rightSum)

            return node.val + max(leftSum,rightSum)

        solve(root)
        return maxi[0]

