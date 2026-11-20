class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        my_map = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            my_map[num] = my_map.get(num, 0) + 1
        for num, freq in my_map.items():
            bucket[freq].append(num)
        result = []
        for i in range(len(bucket) -1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
        