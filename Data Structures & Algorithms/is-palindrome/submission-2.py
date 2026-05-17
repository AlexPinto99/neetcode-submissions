class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, k = 0, len(s) - 1
        while i < k:
            while not self.isAlNum(s[i]) and i<k:
                i += 1
            while not self.isAlNum(s[k]) and k>i:
                k -= 1
            if s[i].lower() != s[k].lower(): return False
            i, k = i+1, k-1
        return True

    def isAlNum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z") or
            ord("a") <= ord(c) <= ord("z") or
            ord("0") <= ord(c) <= ord("9")
        )

