class Solution(object):
    # def findmax(self,height):
    #     m=0
    #     mi=0
    #     l=len(height)
    #     for i in range(l):
    #         if height[i]>m:
    #             m=height[i]
    #             mi=i

    #     return m,mi
    def maxArea(self, height):


        ans=0
        l=len(height)

        le=0
        re=l-1

        while le<re:
            newans = (re-le) * (min(height[le],height[re]))
            ans=max(newans,ans)

            if height[le]<height[re]:
                le+=1
            else:
                re-=1

        return ans



        # for i in range(l):
        #     for j in range(i+1,l):
        #         he=min(height[i],height[j])
        #         le=j-i
        #         newans=le*he
        #         # if newans > ans:
        #         #     ans= newans
        #         ans=max(ans,newans)

        
        # maxno,maxpivot=self.findmax(height)
        # for i in range(l):
        #     if maxpivot>i:
        #         newans=height[i]*(maxpivot-i)
        #     else:
        #         newans=height[i]*(i-maxpivot)


        #     if newans > ans:
        #         ans = newans 

             
                
        # return ans
        """
        :type height: List[int]
        :rtype: int
        """

        # added a comment