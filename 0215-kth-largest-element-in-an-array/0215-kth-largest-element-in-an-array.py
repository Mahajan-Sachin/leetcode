class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=[-num for num in nums]
        heapq.heapify(nums)
        x=-1
        for i in range(k):
            x=-heapq.heappop(nums)
        return x
