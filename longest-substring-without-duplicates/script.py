# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         positions = dict()
#         longest = 0
#         current_length = 0
#         f_position = 0
#         # positions['x'] = 1
#         for position in range(len(s)):
#             if positions.get(s[position]) is not None:
#                 # dump length
#                 if longest < current_length:
#                     longest = current_length
#                 if positions[s[position]] >= f_position:
#                     f_position = positions[s[position]] + 1
#                 current_length = position - f_position
#                 positions[s[position]] = position
#             else:
#                 positions[s[position]] = position
#             current_length += 1
#         if longest > current_length:
#             return longest
#         return current_length


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in p:
                l = max(p[s[r]] + 1, l)
            p[s[r]] = r
            res = max(res, p[s[r]] - l + 1)
        return res

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in p:
                p.remove(s[l])
                l += 1
            p.add(s[r])
            res = max(res, r - l + 1)
        return res

input = ["pwwkew","dvdf","abba","abcabcbb","cdd", "aa", "aab"]
#input = ["aa"]
x = Solution()
for s in input:
    print(s, x.lengthOfLongestSubstring(s))




