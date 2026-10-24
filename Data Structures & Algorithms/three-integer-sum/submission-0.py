class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-1):
            l=i+1
            r=len(nums)-1
            while l<r:
                k=nums[i]+nums[l]+nums[r]
                if k==0:
                    seen=[nums[i],nums[l],nums[r]]
                    if seen not in res:
                        res.append([nums[i],nums[l],nums[r]])
                    r-=1
                    l+=1
                elif k>0:
                    r-=1
                else:
                    l+=1
        return res

        
        