class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        cs={}
        ct={}
        for i in s:
            if i in cs:
                cs[i]+=1
            else:
                cs[i]=1
        for i in t:
            if i in ct:
                ct[i]+=1
            else:
                ct[i]=1
        for i in t:
            if i in s:
                if cs[i]!=ct[i]:
                    return False
            else:
                return False
        return True
        