from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return
        for j in range(len(nums))[::-1]:
            for i in range(j)[::-1]:
                if nums[j] > nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
                    return
        nums.sort()


a = Solution()
a.nextPermutation([1, 2, 3])
