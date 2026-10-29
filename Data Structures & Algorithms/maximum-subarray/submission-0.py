class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        ms=nums[0]
        for num in nums:
            if sum<0:
                sum=0
            sum+=num
            ms=max(ms,sum)
        return ms

        