class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w=0
        for r in range(len(nums)):

            if r!=0 and nums[r]== nums[r-1]:
                pass
            else:
                nums[w]=nums[r]
                w+=1
                
        return w

        