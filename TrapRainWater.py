import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if len(heightMap) == 0 or len(heightMap[0]) == 0:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visit = []
        heap = []
        for x in range(m):
            for y in range(n):
                if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                    heap.append((heightMap[x][y], x, y))
                    visit.append((x, y))

        heapq.heapify(heap)
        result = 0
        while heap:
            height, currentX, currentY = heapq.heappop(heap)
            for x, y in (
            (currentX + 1, currentY), (currentX - 1, currentY), (currentX, currentY + 1), (currentX, currentY - 1)):
                if 0 <= x < m and 0 <= y < n and (x, y) not in visit:
                    result += max(0, height - heightMap[x][y])
                    heapq.heappush(heap, (max(height, heightMap[x][y]), x, y))
                    visit.append((x, y))

        return result

Solution().trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])