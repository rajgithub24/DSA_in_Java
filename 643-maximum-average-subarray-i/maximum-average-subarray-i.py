class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = float(-inf)
        l, r = 0, k-1
        window_sum = sum(nums[l:r+1])
        max_sum = window_sum
        while r < len(nums)-1:
            window_sum-= nums[l]
            l+= 1
            r+= 1
            window_sum+= nums[r]
            max_sum = max(max_sum, window_sum)
        return max_sum/k