class Solution:
    def isPalindrome(self, s: str) -> bool:
        _s = ''
        for i in s:
            if i in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
                _s = _s + i.lower()
        if len(_s) < 2:
            return True
        half = int(len(_s)/2)
        for position in range(half+1):
            if _s[position] != _s[len(_s) - position - 1]:
                return False
        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowed_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        left = 0
        right = len(s) - 1
        while right > left:
            if s[left] not in allowed_list:
                left += 1
            elif s[right] not in allowed_list:
                right -= 1
            elif s[left].upper() != s[right].upper():
                return False
            else:
                left += 1
                right -= 1
        return True
    

x = Solution()
print(x.isPalindrome('race a car'))