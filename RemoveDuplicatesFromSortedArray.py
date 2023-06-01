class Solution(object):
    def removeDuplicates(self, nums):
        l=len(nums)
        i=0

        for j in range(1,l):
            if nums[j]!=nums[i]:
                nums[i+1],nums[j]=nums[j],nums[i+1]
                i+=1

        return i+1
     
            

        
        
        """
        :type nums: List[int]
        :rtype: int
        """