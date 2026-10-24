class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        done={}
        for i in range(len(nums)):
            c=target-nums[i]
            if c in done:
                return [done[c],i]
            else:
                done[nums[i]]=i
        