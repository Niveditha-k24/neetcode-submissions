class Solution:

    def encode(self, strs: List[str]) -> str:
        w=""
        for word in strs:
            w+=str(len(word))+"#"+word
        return w

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i < len(s):
            j=s.find("#",i)
            num=int(s[i:j])
            word=s[j+1:j+1+num]
            res.append(word)
            i=j+1+num
        return res