class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0 or s[0] not in ["(", "[", "{"]: return False
        par = []
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="[" or s[i]=="{":
                par.append(s[i])
            elif len(par) == 0:
                return False
            else:
                last_par = par.pop()
                if last_par == "{":
                    if s[i] != "}":
                        return False
                if last_par == "[":
                    if s[i] != "]":
                        return False
                if last_par == "(":
                    if s[i] != ")":
                        return False
        if len(par) != 0:
            return False
        return True