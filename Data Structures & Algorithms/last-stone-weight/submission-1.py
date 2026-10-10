class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
         - use a max heap. do this by adding negated values into the heap
         - start off by adding all the elements of the array into the heap
         - while the length of the heap is >=2, we should run the simulation
         - return the answer at the end, which is either 0 or heap[0]
        '''

        heap = []
        heapq.heapify(heap)

        for stone in stones:
            heapq.heappush(heap, -1 * stone)
        
        while len(heap) >= 2:
            largest = heapq.heappop(heap) * -1
            second_largest = heapq.heappop(heap) * -1

            if largest == second_largest:
                continue
            else:
                heapq.heappush(heap, (largest - second_largest) * -1)

        if heap:
            return -1 * heap[0]
        
        return 0