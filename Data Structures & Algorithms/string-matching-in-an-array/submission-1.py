class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        i=0
        res=[]
        while i<len(words):
            target=words[i]
            j=0
            while j<len(words):
                if target in words[j] and target!=words[j] and target not in res:
                    res.append(target)
                j+=1
            i+=1
        return res

       
        