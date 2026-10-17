class Solution(object):
    def permute(self, nums):
        result = []
        current = []
        used = [False] * len(nums)

        def backtrack():
            if len(current) == len(nums):
                result.append(current[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue


                current.append(nums[i])
                used[i] = True

                backtrack()

                current.pop()
                used[i] = False

        backtrack()
        return result