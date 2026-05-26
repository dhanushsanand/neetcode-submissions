class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""

        for string in strs:
            encodedString += str(len(string))+ "#" + string

        return encodedString


        # encode = ""
        # for code in strs:
        #     encode += str(len(code)) + "#"
        # return encode

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!="#":
                j+=1
            length = int(s[i:j])
            string = s[(j+1):(j+1+length)]
            res.append(string)
            i = j + length + 1
      
        return res

        


