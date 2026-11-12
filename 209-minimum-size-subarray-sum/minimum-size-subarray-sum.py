class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l, total = 0, 0
        best = len(nums)+1
        for r, num in enumerate(nums):
            total += num
            while total >= target:
                best = min(best, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if best > len(nums) else best
            
        