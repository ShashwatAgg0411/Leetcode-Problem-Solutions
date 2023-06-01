class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n=len(nums)
        ls=0
        rs=sum(nums[1:])
        for i in range(n-1):
            # ls=0
            if ls==rs:
                return i

            ls+=nums[i]
            rs-=nums[i+1]

        if ls==rs:
            return n-1
        

        return -1
            
