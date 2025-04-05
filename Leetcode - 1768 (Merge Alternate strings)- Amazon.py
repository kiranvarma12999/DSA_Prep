class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x = len(word1)
        y= len(word2)
        k = min(x,y)
        new = []
        for i in range (0, k):
            new.append(word1[i])
            new.append(word2[i])
        if x>y:
            word3 = (word1[k:])
            for char in word3:
                new.append(char)
        else:
            word3 = (word2[k:])
            for char in word3:
                new.append(char)
        return ''.join(new) 