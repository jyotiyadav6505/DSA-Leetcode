class Solution(object):
    def rightSideView(self, root):
        ans = []

        def reversePostOrder(node, level, ans):
            if node is None:
                return

            if len(ans) == level:
                ans.append(node.val)

            if node.right:
                reversePostOrder(node.right, level + 1, ans)

            if node.left:
                reversePostOrder(node.left, level + 1, ans)

        reversePostOrder(root, 0, ans)

        return ans