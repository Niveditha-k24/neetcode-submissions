class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for word in strs:
            key=''.join(sorted(word)) #sorted(word) retruns the list of all characters in the word in sorted order so we need to make that string hence join.
            if key in groups:
                groups[key].append(word)
            else:
                groups[key]=[word]
        return list(groups.values())
        

        