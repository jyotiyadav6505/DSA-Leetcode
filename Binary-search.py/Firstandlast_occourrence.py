class Solution(object):
    def searchRange(self, nums, target):
        # First occourrence
        low = 0
        high = len(nums)

        while low < high:
            mid = (low + high)//2
            
            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1

        first = low 

        # Target doesnt exist
        if first == len(nums) or nums[first] != target:
            return [-1,-1]

            # Last occourrence
        low = 0 
        high = len(nums)

        while low < high:
            mid = ( low + high) // 2
            
            if nums[mid] > target:
                high = mid
            else:
                low = mid + 1
            
        last = low - 1

        return [first,last]