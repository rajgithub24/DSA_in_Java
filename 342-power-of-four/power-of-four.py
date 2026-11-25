class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0 or (n & (n-1)) != 0:
            return False
        pos=0
        while n>1:
            n >>= 1
            pos += 1
        return pos%2==0
        