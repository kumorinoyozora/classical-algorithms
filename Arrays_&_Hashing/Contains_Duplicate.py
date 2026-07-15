# https://neetcode.io/problems/duplicate-integer/question


from typing import List


# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         return len(set(nums)) != len(nums)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = dict()
        for el in nums:
            if el not in mp:
                mp[el] = 1
            else:
                return True
        return False


nums = [1, 2, 3, 3]
print(Solution().hasDuplicate(nums))