class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        nearestBike = None
        nearestIndex = -1
        minDis = 2000
        result = []
        for w in enumerate(workers):
            for i, b in [bike for bike in enumerate(bikes) if len(bike) < 3]:
                md = abs(w[0] - b[0]) + abs(w[1] - b[1])
                if md < minDis:
                    minDis = md
                    nearestBike = b
                    nearestIndex = i
            result.append(nearestIndex)
            nearestBike.append(0)
            minDis = 2000
            nearestIndex = -1

        return result