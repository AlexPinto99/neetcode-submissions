class Solution:
    def isPalindrome(self, s: str) -> bool:
        st1 = ""
        for a in s:
            if a.isalnum():
                st1 += a.lower()
        k = len(st1) - 1
        for i in range(len(st1)//2):
            if st1[i] != st1[k]: return False
            k -= 1
        return True