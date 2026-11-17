class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0]*n
        posIdx, negIdx = 0, 1
        for i in range(0, n):
            if nums[i] >= 0:
                result[posIdx] = nums[i]
                posIdx += 2
            else:
                result[negIdx] = nums[i]
                negIdx += 2
        return result
        