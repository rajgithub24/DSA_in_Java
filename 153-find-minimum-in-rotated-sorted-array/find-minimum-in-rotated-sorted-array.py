class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        mini = float(inf)
        l, r = 0, n-1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] <= nums[r]:
                mini = min(mini, nums[mid])
                r = mid - 1
            else:
                mini = min(mini, nums[l])
                l = mid + 1
        return mini
        