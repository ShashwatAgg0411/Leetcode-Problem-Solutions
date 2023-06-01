class Solution(object):
    def twoSum(self, nums, target):

        
        
        l=len(nums)
        for i in range(l):
            for j in range(i+1,l):
                if nums[i]+nums[j]==target:
                    li=[i,j]
                    return li
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
     
    
    
