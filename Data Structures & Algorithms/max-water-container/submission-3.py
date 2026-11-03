class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        ma=0
        while l<r:
            w=r-l
            h=min(heights[l],heights[r])
            a=w*h
            ma=max(a,ma)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return ma

        
        