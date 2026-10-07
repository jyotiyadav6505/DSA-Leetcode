class Solution(object):
    def subsets(self, nums):
        result = []

        def solve(index,current):
            if index == len(nums):
                result.append(current[:])
                return

            current.append(nums[index])
            solve(index + 1, current)

            current.pop()
            solve(index + 1,current)

        solve(0,[])
        return result

