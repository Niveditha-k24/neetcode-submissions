class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        ml=height[l]
        mr=height[r]
        amt=0
        while l<r:
            if ml<mr:
                l+=1
                ml=max(ml,height[l])
                amt+=ml-height[l]
            else:
                r-=1
                mr=max(mr,height[r])
                amt+=mr-height[r]
        return amt
        
        


        
        