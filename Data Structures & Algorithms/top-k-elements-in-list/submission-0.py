import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_heap = []
        my_hashmap = {}

        for num in nums:
            my_hashmap[num] = my_hashmap.get(num,0) + 1
        
        for value, key in my_hashmap.items():
            heapq.heappush(my_heap, (key,value))
            if len(my_heap) > k:
                heapq.heappop(my_heap)
        
        return [pair[1] for pair in my_heap]
        