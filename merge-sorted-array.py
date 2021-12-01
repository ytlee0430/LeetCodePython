from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 1
        for num in nums:
            if nums[i-1] < num:
                i += 1
                nums[i] = num
        return i

Solution().removeDuplicates([1, 1, 2])