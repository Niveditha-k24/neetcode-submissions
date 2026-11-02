class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        res=[]
        n=len(nums)
        for i in count:
            if count[i]>(n//3):
                res.append(i)
        return res        