class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        mc=0
        for num in nums:
            if num-1 not in nums:
                start=num
                c=1
                while start+1 in nums:
                    c+=1
                    start=start+1
                mc=max(c,mc)
            
        return mc
                
           
        