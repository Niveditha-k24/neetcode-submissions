class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mc=0
        num=set(nums)
        for i in num:
            if i-1 not in num:
                start=i
                c=1
                while start+1 in num:
                    c+=1
                    start=start+1
                mc=max(c,mc)
            
        return mc


        