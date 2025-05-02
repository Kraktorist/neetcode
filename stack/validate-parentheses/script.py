class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        pairs = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }
        for i in range(len(s)):
            letter = s[i]
            if letter in '({[':
                stack.append(letter)
            elif len(stack):
                if stack.pop() != pairs[letter]:
                    return False
            else:
                return False
        return not len(stack)
