class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        res = 0
        for num in nums:
            if count == 0:
                res = num
            if num == res:
                count+=1
            else:
                count-=1
        return res
        
        # T(n)
        # S(1)