class Solution:
    def encode(self, strs: List[str]) -> str:
        s=""
        for word in strs:
            s+=str(len(word))+"#"+word
        return s
      
    def decode(self, s: str) -> List[str]:
        strings=[]
        i=0
        while i<len(s):
            j=s.find("#",i)
            num=int(s[i:j])
            word=s[j+1:j+num+1]
            strings.append(word)
            i=j+num+1
        return strings


        