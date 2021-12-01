from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == 1 or len(arr) <= k:
            return arr

        min_dis = 10000
        min_index = 0

        for i in range(len(arr)):
            dis = abs(arr[i] - x)
            if min_dis >= dis:
                min_dis = dis
                min_index = i

        left = max(min_index - k, 0)
        right = min(min_index + k, len(arr) - 1)
        while (k < right - left):
            dis_right = arr[right] - x
            dis_left = x - arr[left]
            if (arr[right] - x >= x - arr[left]):
                right -= 1
            else:
                left += 1

        return arr[left:right]


Solution().findClosestElements([0,0,0,1,3,5,6,7,8,8],2,2)



