from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxDuring = releaseTimes[0]
        maxIndex = 0
        for index in range(1, len(releaseTimes)):
            diff = releaseTimes[index] - releaseTimes[index - 1]
            if diff > maxDuring or (diff == maxDuring and keysPressed[maxIndex] > keysPressed[index]):
                maxDuring = diff
                maxIndex = index

        return keysPressed[maxIndex]

Solution().slowestKey([23,34,43,59,62,80,83,92,97],"qgkzzihfc")

