class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        for i,j in zip(word1,word2):
            s+=i+j
        s+=word1[len(word2):]
        s+=word2[len(word1):]
        return s