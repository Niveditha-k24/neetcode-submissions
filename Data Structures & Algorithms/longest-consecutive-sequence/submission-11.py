class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mc=0
        num_set=set(nums)
        for no in num_set:
            if no-1 in num_set:
                pass
            else:
                start=no
                c=1
                while start+1 in num_set:
                    c+=1
                    start=start+1
                mc=max(mc,c)
        return mc



        


        