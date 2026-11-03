class Solution:
    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=str(len(i))+"#"+i
        return s
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<(len(s)):
            j=s.find("#",i)
            n=int(s[i:j])
            word= s[j+1:j+n+1] 
            res.append(word)
            i=j+n+1
        return res
            

            


    

        


        