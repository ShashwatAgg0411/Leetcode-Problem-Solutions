class Solution(object):
    def runningSum(self, nums):
        sum=0
        n=len(nums)
        for i in range(n):
            nums[i]+=sum
            sum=nums[i]


        return nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """