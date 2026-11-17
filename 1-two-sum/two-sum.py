class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        n = len(nums)
        for i in range(0, n):
            rem = target - nums[i]
            if rem in hash_map:
                return [hash_map[rem], i]
            hash_map[nums[i]] = i         

        