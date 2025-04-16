class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        vocab = dict()
        l = 0
        longest = 0
        most_repeatable = 0
        for r in range(len(s)):
            vocab[s[r]] = vocab.get(s[r], 0) + 1
            most_repeatable = max(most_repeatable, vocab[s[r]])
            while r - l - k - most_repeatable + 1 > 0:
                vocab[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest


input = [
    ["BAAA",0],
    ["ABBB",2],
    ["XYYX",2],
    ["AAABABB",1]
]


x = Solution()
for s in input:
    print(s, x.characterReplacement(s[0],s[1]))
