class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_seen = {}
        count, r, curr_sum = 0, 0, 0
        for r in range(len(nums)):
            prefix_seen[curr_sum] = 1 + prefix_seen.get(curr_sum, 0)
            curr_sum+= nums[r]
            if (curr_sum - k) in prefix_seen:
                count+= prefix_seen[curr_sum - k]
            r += 1
        return count
        