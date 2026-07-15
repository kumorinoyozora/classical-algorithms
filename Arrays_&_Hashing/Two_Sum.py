# https://neetcode.io/problems/two-integer-sum/question


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, num in enumerate(nums): # enumerate эффективнее по памяти чем range
            diff = target - num
            if diff in mp:
                return [mp[diff], i]
            mp[num] = i
        return []


nums = [3,4,5,6]
target = 7
print(Solution().twoSum(nums, target))