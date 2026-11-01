class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long=set()
        l=0
        res=0
        for i in range(len(s)):
            while s[i] in long:
                long.remove(s[l])
                l+=1
            long.add(s[i])
            res=max(res,len(long))
        return res
            

        

        

        
            
            
