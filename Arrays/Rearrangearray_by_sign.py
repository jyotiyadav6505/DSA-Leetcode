class Solution(object):
    def rearrangeArray(self, nums):
       n = len(nums)
       result = [0] * n
       Pos_index,Neg_index = 0,1
       for i in range (0,n):
        if nums [i] >= 0:
            result [Pos_index] = nums[i]
            Pos_index +=2
        else:
            result [Neg_index] = nums[i]
            Neg_index +=2

       return result
