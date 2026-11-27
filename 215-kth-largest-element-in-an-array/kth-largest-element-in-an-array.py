class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = [] #create heap
        for num in nums: #we push elenemnt in heap
            heapq.heappush(heap, num)
            if len(heap) > k: #if number of element if greater thrn k we pop thr third element
                heapq.heappop(heap)
        return heap[0] #top element is kth largest element
        