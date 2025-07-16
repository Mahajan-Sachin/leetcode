import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        heapq.heapify(heap)
        for num in arr:
            diff=num-x
            heapq.heappush(heap,(-abs(diff),-num)) # sabse pehla diff ka basis pa heap bna maximim value delete hogi
            if len(heap)>k:
                heapq.heappop(heap)
        new_heap=[-val for (key,val) in heap]
        new_heap.sort()
        return new_heap

        