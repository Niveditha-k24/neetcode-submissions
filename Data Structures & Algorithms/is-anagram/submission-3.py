class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ct={}
        cs={}
        if len(s)!=len(t):
            return False
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
        for i in cs:
            if i not in ct or ct[i]!=cs[i]:
                return False
        return True

        