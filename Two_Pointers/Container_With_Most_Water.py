# https://neetcode.io/problems/max-water-container/question?list=neetcode150


from typing import List

# If heights[i] is smaller, then any future container using index i will have 
# a smaller width, and its height is still at most heights[i]. So it cannot produce 
# a larger area than the current pair. Therefore, we can safely discard the 
# smaller height and move that pointer inward. The same logic applies when 
# heights[j] is smaller.


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_square = 0
        while left < right:
            current_square = min(heights[left], heights[right]) * (right - left)
            if current_square > max_square:
                max_square = current_square
            elif heights[left] < heights[right]:
                left += 1
            else: 
                right -= 1
        return max_square


inp = [1,7,2,5,12,3,500,500,7,8,4,7,3,6]

sol = Solution()
print(sol.maxArea(inp))