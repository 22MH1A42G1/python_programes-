##import math
##class Solution:
##    def isPerfectSquare(self, num: int) -> bool:
##        return math.isqrt(num) ** 2 == num
##    def numSquares(self, n: int) -> int:
##        while n % 4 == 0:
##            n //= 4
##        if n % 8 == 7:
##            return 4
##        if self.isPerfectSquare(n):
##            return 1
##        for i in range(1, int(math.isqrt(n)) + 1):
##             if self.isPerfectSquare(n - i * i):
##                return 2
##        return 3
##s = Solution()
##n = int(input())
##r = s.numSquares(n)
##print( r)

class Solution:
    def reversestr(s):
        return s
a=Solution()
s=list(map(str,input().split()))
print(s.reversestr)














