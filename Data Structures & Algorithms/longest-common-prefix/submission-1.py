class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        pre = ""
        init = strs[0]

        for i in range(len(init)):
            for s in strs:
                if i >= len(s) or init[i] != s[i]:
                    return pre

            pre += init[i]

        return pre