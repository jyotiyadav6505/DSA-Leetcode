class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def solve(index,current,total):

            if total == target:
                result.append(current[:])
                return

            for i in range(index,len(candidates)):

                if i > index and candidates[i] == candidates[i-1]:
                    continue

                if total + candidates[i] > target:
                    break
                    

                current.append(candidates[i])

                solve(i+1, current, total + candidates[i])

                current.pop()

        solve(0,[],0)

        return result
        