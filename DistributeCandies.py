class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        d={}
        caneat=len(candyType)//2
        ans=0
        for ele in candyType:

            if caneat==0:
                return ans
            if d.get(ele) is None:
                d[ele]=1
                caneat-=1
                ans+=1

        return ans


