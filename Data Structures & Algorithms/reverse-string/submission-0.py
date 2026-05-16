class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        k = len(s) - 1
        j = 0

        for i in range(len(s)//2):
            j = s[i]
            s[i] = s[k]
            s[k] = j
            k -= 1

        