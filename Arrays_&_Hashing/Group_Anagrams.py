# https://neetcode.io/problems/anagram-groups/question


from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # mp = defaultdict(list)
        mp = dict()
        for s in strs:
            count = [0] * (ord("z") - ord("a") + 1)
            for c in s:
                count[ord(c) - ord("a")] += 1
            # mp[tuple(count)].append(s)
            mp.setdefault(tuple(count), []).append(s)
        return list(mp.values())


strs = ["act","pots","tops","cat","stop","hat"]

print(Solution().groupAnagrams(strs))

# алгоритм поиска анограммы к таргету
# каждую строку записывать в хэшмэп по ключу - словарь частотностей, таким образом группируя анограммы
