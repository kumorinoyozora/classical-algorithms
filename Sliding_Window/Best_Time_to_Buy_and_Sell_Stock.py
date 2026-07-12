# https://neetcode.io/problems/buy-and-sell-crypto/question?list=neetcode150


from typing import List

# O(n) O(1)
# two pointers
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         left, right = 0, 1
#         maxP = 0
#         while right < len(prices):
#             if prices[left] < prices[right]:
#                 profit = prices[right] - prices[left]
#                 maxP = max(maxP, profit)
#             else:
#                 left = right
#             right += 1
#         return maxP

# O(n^2) O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for i in range(1, len(prices)):
            profit = prices[i] - min(prices[:i])
            maxP = max(maxP, profit)
        return maxP


prices = [10,1,5,6,7,1]

print(Solution().maxProfit(prices))