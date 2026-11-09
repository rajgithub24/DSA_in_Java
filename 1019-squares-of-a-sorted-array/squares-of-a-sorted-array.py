class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l,r = 0, len(nums)-1
        result = [0]*len(nums)
        idx = len(nums)-1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                result[idx] = nums[l]**2
                l +=1
            else:
                result[idx] = nums[r]**2
                r -=1
            idx -=1
        return result                                  