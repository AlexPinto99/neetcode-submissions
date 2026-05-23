class Solution:
    def isValid(self, s: str) -> bool:
        par = []
        correspondingPar = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for p in s:
            if p == "{" or p=="[" or p=="(":
                par.append(p)
            elif par and correspondingPar[p] == par[-1]:
                par.pop()
            else:
                return False
                
        return True if not par else False