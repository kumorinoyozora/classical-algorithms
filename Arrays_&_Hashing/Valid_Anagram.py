# https://neetcode.io/problems/is-anagram/question


# Time complexity: O(n + m)
# Space complexity: O(1) since we have at most 26 different characters.
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         mp1 = {}
#         mp2 = {}
#         for i in range(len(s)):
#             mp1[s[i]] = mp1.get(s[i], 0) + 1
#             mp2[t[i]] = mp2.get(t[i], 0) + 1
#         return mp1 == mp2


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] += 1
            count[ord(t[i]) - ord("a")] -= 1
        
        for val in count:
            if val != 0:
                return False
        return True


s = 'racecar'
t = "carrace"

s = "jar"
t = "jam"

print(Solution().isAnagram(s, t))