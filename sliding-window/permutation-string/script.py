class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = dict()
        for i in range(len(s1)):
            s1_dict[s1[i]] = s1_dict.setdefault(s1[i], 0) + 1
        l = 0
        found = len(s1)

        for r in range(len(s2)):
            while r - l > len(s1) or s1_dict.get(s2[r], 1) <= 0 or (r - l >= 0 and s2[r] not in s1_dict.keys()):
                if s2[l] in s1_dict.keys():
                    s1_dict[s2[l]] += 1
                    found += 1
                l += 1
            if s2[r] in s1_dict.keys():
                found -= 1
                s1_dict[s2[r]] -= 1
            if found == 0:
                return True
        return False


"""
r         0  1  2  4  5  6  7  8                
s[r]      l  e  c  a  a  b  e  e
l         0  0  0  
found     0  0  1  2


    abc
"""

input = [
    ["ab","eidboaoo"],
    ["abc", "lecaabee"],
    ["abc", "lecabee"]
]
#input = ["aa"]
x = Solution()
for s in input:
    print(s, x.checkInclusion(s[0], s[1]))