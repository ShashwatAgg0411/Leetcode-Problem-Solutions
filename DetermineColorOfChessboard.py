class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        a=coordinates[0]
        b=int(coordinates[1])

        if (b%2==0) and (a=='a' or a=='c' or a=='e' or a=='g'):
            return True
        
        elif b%2!=0 and(a=='b' or a=='d' or a=='f' or a=='h'):
            return True

        return False

        