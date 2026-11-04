class Solution:
    def compress(self, chars: List[str]) -> int:
        w=0
        r=0
        i=0
        while i <len(chars):
            char=chars[i]
            count=0
            while i<len(chars) and chars[i]==char:
                count+=1
                i+=1
            chars[w]=char
            w+=1
            if count>1:
                for dig in str(count):
                    chars[w]=dig
                    w+=1
        return w
        

        