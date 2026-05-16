class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        k = len(s) - 1
        for i in range(len(s)//2):
            s[i], s[k] = s[k], s[i]
            k -= 1

        