class Solution:

    def convert(self,n,k,sum):
        if n<k:
            sum+=n
            return sum
        remainder=n%k
        sum+=remainder
        quo=n//k
        a=self.convert(quo,k,sum)
        return a
        # return (10*a)+remainder
    def sumBase(self, n: int, k: int) -> int:
        sum=0
        
        basek=self.convert(n,k,sum)
        return basek
        # for ele in str(basek):
        #     sum+=int(ele)

        # return sum