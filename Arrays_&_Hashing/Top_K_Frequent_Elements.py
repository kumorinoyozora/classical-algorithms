# https://neetcode.io/problems/top-k-elements-in-list/question


from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        
        for num in nums:
            count[num] = count.get(num, 0) + 1 # считаем частоту
        for num, cnt in count.items(): 
            freq[cnt].append(num) # раскидываем по бакетам
        
        q = 0
        res = []
        for bckt in freq[::-1]:
            for num in bckt:
                res.append(num)
                q += 1
                if q == k:
                    return res
        return res



nums = [1,2,2,3,3,3]
k = 2
print(Solution().topKFrequent(nums, k))