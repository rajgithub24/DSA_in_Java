class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        i = 0
        while (i < n):
            nums[i], nums[i+1] = nums[i+1], nums[i]
            i += 2
        return nums
        