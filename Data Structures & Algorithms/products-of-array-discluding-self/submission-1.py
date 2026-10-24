class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=1
        suff=1
        res=[]
        for num in nums:
            res.append(pre)
            pre*=num
        for i in range(len(nums)-1,-1,-1):
            res[i]*=suff
            suff*=nums[i]
        return res
    
    
        