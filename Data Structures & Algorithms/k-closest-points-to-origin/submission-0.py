class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        heapq.heapify(max_heap)

        for point in points:
            x, y = point
            distance = math.sqrt(math.pow(x, 2) + math.pow(y,2))
            heapq.heappush(max_heap, (-1 * distance, point))
            
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        ans = []
        for element in max_heap:
            ans.append(element[1])
        return ans
