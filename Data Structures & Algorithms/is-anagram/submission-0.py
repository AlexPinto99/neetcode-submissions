class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashMap = {}

        for c in s:
            if c not in hashMap:
                hashMap[c] = 1
            else: hashMap[c] += 1

        for c in t:
            if c not in hashMap:
                return False
            hashMap[c] -= 1

        for elem in hashMap.values():
            if elem != 0:
                return False

        return True


s="racecar"
t="carrace"

soluzione = Solution()
anagramma = soluzione.isAnagram(s,t)
