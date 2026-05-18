class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, k = 0, len(s) - 1
        while i<k:
            if s[i] != s[k]:
                sL = s[i+1:k+1]
                sR = s[i:k]
                return(sL == sL[::-1] or sR == sR[::-1])
            i, k = i+1, k-1
        return True