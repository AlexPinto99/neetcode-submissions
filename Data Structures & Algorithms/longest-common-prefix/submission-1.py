class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        num_words = len(strs)
        if num_words==1:
            return strs[0]
        if (len(strs[0])==0) or (len(strs[1])==0):
            return ""
        if strs[0][0]==strs[1][0]:
            length = len(strs[0])
        else: return ""

        initials = ""

        for i in range(1, len(strs)):
            new_length = len(strs[i])
            if new_length<length:
                length = new_length

        initials = strs[0][0:length]


        for i in range(length-1, 0, -1 ):
            for j in range(1, num_words):
                if initials[i] != strs[j][i]:
                    initials = initials[0:i]
                    break

        return initials