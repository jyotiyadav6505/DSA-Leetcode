class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def solve(index, current, total):

            if total == target:
                result.append(current[:])
                return

            if index == len(candidates) or total > target:
                return

            # Take
            current.append(candidates[index])
            solve(index, current, total + candidates[index])

            # Undo
            current.pop()

            # Don't take
            solve(index + 1, current, total)

        solve(0, [], 0)

        return result