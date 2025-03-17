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
        cur_len = 0
        max_len = 0
        pos = 0
        letters = list()
        for i in range(len(s)):
            if s[i] not in letters:
                letters.add(s[i])
                cur_len += 1
            else:
                max_len = max(max_len, cur_len)
                cur_len = i - pos 
                pos = i
        return max(cur_len, max_len)

input = ["pwwkew","dvdf","abba","abcabcbb","cdd", "aa", "aab"]
#input = ["aa"]
x = Solution()
for s in input:
    print(s, x.lengthOfLongestSubstring(s))




