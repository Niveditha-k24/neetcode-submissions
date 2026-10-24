class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(numbers)):
            c=target-numbers[i]
            if c in seen and seen[c]<i:
                return [seen[c]+1,i+1]
            else:
                seen[numbers[i]]=i
        