class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        curr=0
        presums={0:1}
        for n in nums:
            curr+=n
            diff=curr-k
            res+=presums.get(diff,0)
            presums[curr]=1+presums.get(curr,0)
        return res
       

            

        
        