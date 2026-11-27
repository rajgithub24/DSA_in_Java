class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1]*n
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]
        rightProd = 1
        
        for i in range(n-1, -1, -1):
            ans[i] = ans[i] * rightProd
            rightProd*= nums[i]
        return ans
        