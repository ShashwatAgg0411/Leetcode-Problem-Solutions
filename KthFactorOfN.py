class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # if n==0:
        #     return -1
        count=1
        for i in range(1,n+1):
            if n%i==0:
                if count==k:
                    return i
                count+=1
        return -1