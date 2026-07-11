# https://neetcode.io/problems/two-integer-sum-ii/question?list=neetcode150


from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            num_sum = numbers[start] - numbers[end]
            if num_sum == target:
                return [start+1, end+1]
            elif num_sum < target:
                start += 1
            else:
                end -= 1
        return []


numbers = [1, 2, 3, 4]
target = 3

solution = Solution()
print(solution.twoSum(numbers, target))
