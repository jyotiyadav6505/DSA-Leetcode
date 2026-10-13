class Solution(object):
    def combinationSum3(self, k, n):
        result = []

        def solve(start, current, total):

            if len(current) == k:
                if total == n:
                    result.append(current[:])
                return

            for i in range(start, 10):

                if total + i > n:
                    break

                current.append(i)

                solve(i + 1, current, total + i)

                current.pop()

        solve(1, [], 0)
        return result