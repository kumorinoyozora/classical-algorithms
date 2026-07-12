# https://neetcode.io/problems/longest-substring-without-duplicates/question?list=neetcode150


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_idx = dict()
        longest = 0
        l = 0

        for r in range(len(s)):
            if s[r] in last_idx:
                l = max(last_idx[s[r]] + 1, l)
            last_idx[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest


s = "zyxzxyz"

print(Solution().lengthOfLongestSubstring(s))