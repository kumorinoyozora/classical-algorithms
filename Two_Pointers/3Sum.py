# https://neetcode.io/problems/three-integer-sum/question?list=neetcode150


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = list()

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                num_sum = nums[i] + nums[left] + nums[right]
                if num_sum < 0:
                    left += 1
                elif num_sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # skip duplicates 
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result


nums=[0,0,0,0]


sol = Solution()
print(sol.threeSum(nums))

